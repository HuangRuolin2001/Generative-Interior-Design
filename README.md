Generative Interior Design: AI-Driven Space Transformation

Objective
This project sought to investigate practical applications of generative AI in interior design, focusing on developing systems that:
Convert empty room images into furnished spaces using text guidance
Support basic iterative refinement capabilities
Help bridge conceptual and visual representations in early design phases

Approach
Our team's entry explored several technical directions:
1.Conditional Generation: Combined open-source Stable Diffusion models with ControlNet implementations
  Utilized semantic segmentation (UperNet) for spatial understanding
  Tested edge preservation techniques for structural consistency
2.Dataset Curation: Processed LAION subset with:
  Automated captioning via BLIP model
  Room-type classification using existing architectures
  Style tagging through CLIP embeddings
3.Interactive Prototype: Developed a Gradio interface supporting:
  Basic inpainting functionality
  Style transfer experiments
  Multi-step generation workflows

Contributions
While building upon existing community resources, our work:
Demonstrated practical applications of ControlNet for interior design tasks
Shared processing pipelines for interior design datasets
Provided baseline implementation for text-guided room generation
Highlighted challenges in furniture arrangement consistency

Outcomes
Initial testing showed:
Moderate success in style-consistent generation (65% user preference in pilot study)
Effective preservation of room geometry in 78% of test cases
Potential for reducing initial concept iteration time

Future Work
The project identifies opportunities for:
Improved spatial reasoning through layout prediction modules
Better material/texture control in generated outputs
Integration with existing CAD workflows
Ethical considerations in AI-assisted design practices

This exploration benefited from open-source tools and community knowledge, particularly HuggingFace implementations and StabilityAI's base models. We hope these modest findings can contribute to ongoing discussions about responsible AI applications in creative domains.
