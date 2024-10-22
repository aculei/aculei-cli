import os
from PIL import Image
import pandas as pd
from tqdm import tqdm
from transformers import pipeline

import stages.hasher as hasher
import stages.metadata as metadata
import stages.animal as animal

import typer


DIRECTORY = "./images"
os.environ["TOKENIZERS_PARALLELISM"] = "false"
app = typer.Typer(help="aculei cli 🦔", add_completion=False)


@app.command()
def aculei(
    ocr: bool = typer.Option(False, help="Enable optical character recognition"),
    input_dir: str = typer.Option(DIRECTORY, help="Input directory containing images"),
    output_dir: str = typer.Option(None, help="Output directory for the CSV file")
):
    model = "openai/clip-vit-large-patch14"
    detector = pipeline(model=model, task="zero-shot-image-classification")

    df = pd.DataFrame(columns=["id", "camera", "datetime", "moon_phase", "animal"])

    if not os.path.exists(input_dir):
        typer.echo(f"Input directory {input_dir} does not exist.")
        raise typer.Exit(code=1)

    for image in tqdm(os.listdir(input_dir), desc="Processing images"):
        image_path = os.path.join(input_dir, image)

        with Image.open(image_path) as img:
            id = hasher.generate_md5_image_id(img)

            image_metadata = metadata.get_image_metadata(img)

            # TODO: Attempt OCR on the image for further metadata extraction
            if ocr:
                pass

            prediction = animal.classify(img, detector=detector)       

            df = pd.concat([df, pd.DataFrame([
                        [id, 
                        image_metadata.get('camera', None),
                        image_metadata.get('datetime', None), 
                        image_metadata.get('moon_phase', None), 
                        prediction]], columns=df.columns)], 
                ignore_index=True)
    
    output_dir = output_dir or os.getcwd()
    save_path = os.path.join(output_dir, "aculei.csv")
    df.to_csv(save_path, index=False)
    typer.echo(f"Results saved to {save_path}")


if __name__ == "__main__":
    app()