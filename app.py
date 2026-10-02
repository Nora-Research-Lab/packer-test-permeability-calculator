import gradio as gr
from packer_test_permeability_calculator import (
    lugeon_value,
    hydraulic_conductivity_constant_head,
    hydraulic_conductivity_falling_head,
    permeability_classification,
    lugeon_classification
)
import math

def calculate(L, D_mm, P_bar, Q_Lmin, test_type, d_mm, h1, h2, t):
    # Validate inputs that are always required
    try:
        L = float(L)
        D_mm = float(D_mm)
        P_bar = float(P_bar)
        Q_Lmin = float(Q_Lmin)
    except (TypeError, ValueError):
        return ("Invalid numeric input", "", "", "")
    if L <= 0 or D_mm <= 0 or P_bar <= 0 or Q_Lmin < 0:
        return ("Values must be positive (Q can be zero)", "", "", "")
    
    # Compute Lugeon
    try:
        lu = lugeon_value(Q_Lmin, L, P_bar)
    except ZeroDivisionError:
        return ("Division by zero: L or P zero", "", "", "")
    
    # Compute K
    if test_type == "Constant head":
        try:
            K = hydraulic_conductivity_constant_head(Q_Lmin, L, D_mm/1000, P_bar)  # D in m
        except ZeroDivisionError:
            return ("Division by zero in K calculation", "", "", "")
    else:  # Falling head
        try:
            d_mm = float(d_mm)
            h1 = float(h1)
            h2 = float(h2)
            t = float(t)
        except (TypeError, ValueError):
            return ("Invalid falling head inputs (d, h1, h2, t)", "", "", "")
        if d_mm <= 0 or h1 <= 0 or h2 <= 0 or t <= 0:
            return ("Falling head inputs must be positive", "", "", "")
        if h2 >= h1:
            return ("Final head (h2) must be less than initial head (h1)", "", "", "")
        try:
            K = hydraulic_conductivity_falling_head(d_mm/1000, h1, h2, t, L, D_mm/1000)
        except ZeroDivisionError:
            return ("Division by zero in K calculation", "", "", "")
    
    # Classifications
    perm_class = permeability_classification(K)
    lu_class = lugeon_classification(lu)
    
    # Format outputs
    lu_str = f"{lu:.1f}"
    K_str = f"{K:.2e}"
    
    return lu_str, K_str, perm_class, lu_class

def build_ui():
    with gr.Blocks(title="Packer Test Permeability Calculator") as demo:
        gr.Markdown("## Packer Test Permeability Calculator")
        gr.Markdown("Calculate Lugeon value, hydraulic conductivity, and permeability classification from packer test data.")
        with gr.Row():
            with gr.Column():
                L = gr.Number(label="Test section length (L, m)", value=1.0)
                D = gr.Number(label="Borehole diameter (D, mm)", value=76.0)
                P = gr.Number(label="Injection pressure (P, bar)", value=5.0)
                Q = gr.Number(label="Flow rate (Q, L/min)", value=10.0)
                test_type = gr.Dropdown(["Constant head", "Falling head"], label="Test type", value="Constant head")
                with gr.Column(visible=False) as falling_inputs:
                    d = gr.Number(label="Standpipe inner diameter (d, mm)", value=25.0)
                    h1 = gr.Number(label="Initial head (h1, m)", value=10.0)
                    h2 = gr.Number(label="Final head (h2, m)", value=5.0)
                    t = gr.Number(label="Elapsed time (t, s)", value=60.0)
                btn = gr.Button("Calculate")
            with gr.Column():
                lu_out = gr.Textbox(label="Lugeon value (Lu)", interactive=False)
                K_out = gr.Textbox(label="Hydraulic conductivity (m/s)", interactive=False)
                perm_class_out = gr.Textbox(label="Permeability classification", interactive=False)
                lu_class_out = gr.Textbox(label="Lugeon classification", interactive=False)
        
        def toggle_falling_inputs(choice):
            return gr.update(visible=(choice == "Falling head"))
        test_type.change(toggle_falling_inputs, test_type, falling_inputs)
        
        btn.click(
            calculate,
            inputs=[L, D, P, Q, test_type, d, h1, h2, t],
            outputs=[lu_out, K_out, perm_class_out, lu_class_out]
        )
    return demo

if __name__ == "__main__":
    demo = build_ui()
    demo.launch(server_name="0.0.0.0", server_port=7860)
