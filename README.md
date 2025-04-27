# Generative Interior Design

## 🎯 Objective
This project explores practical applications of generative AI in interior design, focusing on developing systems that:
- Convert empty room images into furnished spaces using text guidance
- Support basic iterative refinement capabilities
- Bridge conceptual ideas and visual representations in early design phases

## 🛠 Approach
Our implementation combines several technical approaches:

### 1. Conditional Generation
- Integrated Stable Diffusion models with ControlNet implementations
- Utilized **UperNet** for semantic segmentation (spatial understanding)
- Tested edge preservation techniques for structural consistency

### 2. Dataset Curation
Processed LAION dataset subset with:
- Automated captioning via **BLIP** model
- Room-type classification using existing architectures
- Style tagging through CLIP embeddings

### 3. Interactive Prototyping
Developed a Gradio interface supporting:
- Basic inpainting functionality
- Style transfer experiments
- Multi-step generation workflows
