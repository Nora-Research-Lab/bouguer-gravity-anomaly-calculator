import gradio as gr
import pandas as pd
from bouguer_gravity_anomaly_calculator import calculate_bouguer_anomaly

def run_calculation(latitude, elevation, observed_gravity, reduction_density=2.67, terrain_correction=0.0):
    try:
        # Validate inputs
        if latitude is None or elevation is None or observed_gravity is None:
            raise ValueError("All required fields must be filled")
        
        result = calculate_bouguer_anomaly(
            latitude, elevation, observed_gravity, reduction_density, terrain_correction
        )
        
        # Prepare data for display
        data = {
            "Parameter": [
                "Theoretical Gravity (mGal)",
                "Free-Air Correction (mGal)",
                "Bouguer Correction (mGal)",
                "Free-Air Anomaly (mGal)",
                "Simple Bouguer Anomaly (mGal)",
                "Complete Bouguer Anomaly (mGal)"
            ],
            "Value": [
                round(result['g_theory'], 3),
                round(result['free_air_correction'], 3),
                round(result['bouguer_correction'], 3),
                round(result['free_air_anomaly'], 3),
                round(result['simple_bouguer_anomaly'], 3),
                round(result['complete_bouguer_anomaly'], 3)
            ]
        }
        
        df = pd.DataFrame(data)
        return df
    except Exception as e:
        return pd.DataFrame({"Error": [str(e)]})

with gr.Blocks() as demo:
    gr.Markdown("# Bouguer Gravity Anomaly Calculator")
    gr.Markdown("Calculate gravity corrections and anomalies for a single ground gravity station.")
    
    with gr.Row():
        latitude = gr.Number(label="Latitude (decimal degrees)", value=45.0)
    with gr.Row():
        elevation = gr.Number(label="Station Elevation (metres)", value=100.0)
    with gr.Row():
        observed_gravity = gr.Number(label="Observed Gravity (mGal)", value=980000.0)
    with gr.Row():
        reduction_density = gr.Number(label="Reduction Density (g/cm³)", value=2.67)
    with gr.Row():
        terrain_correction = gr.Number(label="Terrain Correction (mGal)", value=0.0)
    
    calculate_btn = gr.Button("Calculate")
    
    output = gr.Dataframe(label="Results")
    
    calculate_btn.click(
        fn=run_calculation,
        inputs=[latitude, elevation, observed_gravity, reduction_density, terrain_correction],
        outputs=output
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
