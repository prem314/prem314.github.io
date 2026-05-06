#!/usr/bin/env python3

import argparse
from pathlib import Path

from PIL import Image, ImageEnhance, ImageOps


# Ordered from darkest to brightest for a dark background.
# Spaces represent dark pixels, dense characters represent bright pixels.
ASCII_CHARS = " .,:;irsXA253hMHGS#9B&@"


def resize_image(image: Image.Image, width: int, aspect_scale: float) -> Image.Image:
    """
    Resize image while compensating for character aspect ratio.
    Terminal characters are usually taller than they are wide,
    so the height is scaled down.
    """
    original_width, original_height = image.size
    aspect_ratio = original_height / original_width
    new_height = max(1, int(width * aspect_ratio * aspect_scale))

    return image.resize((width, new_height), Image.Resampling.LANCZOS)


def should_invert(image: Image.Image) -> bool:
    """
    Light LaTeX pages need inversion: black marks become bright characters
    and the white page becomes blank dark editor background.
    """
    histogram = image.histogram()
    pixel_count = image.width * image.height
    brightness_sum = sum(value * count for value, count in enumerate(histogram))
    mean_brightness = brightness_sum / pixel_count

    return mean_brightness > 127


def pixel_to_char(pixel_value: int, chars: str) -> str:
    """Convert a grayscale pixel value, 0 to 255, into one text character."""
    index = int(pixel_value / 255 * (len(chars) - 1))
    return chars[index]


def image_to_ascii(
    path: str,
    width: int = 100,
    chars: str = ASCII_CHARS,
    aspect_scale: float = 0.45,
    contrast_cutoff: int = 1,
    contrast: float = 1.25,
    invert: str = "auto",
) -> str:
    image = Image.open(path)
    image = ImageOps.exif_transpose(image).convert("L")

    if invert == "auto":
        do_invert = should_invert(image)
    else:
        do_invert = invert == "yes"

    if do_invert:
        image = ImageOps.invert(image)

    image = ImageOps.autocontrast(image, cutoff=contrast_cutoff)
    image = ImageEnhance.Contrast(image).enhance(contrast)
    image = resize_image(image, width, aspect_scale)

    converted = [pixel_to_char(pixel, chars) for pixel in image.tobytes()]

    lines = []
    for i in range(0, len(converted), image.width):
        lines.append("".join(converted[i : i + image.width]).rstrip())

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert an image into ASCII art tuned for dark nvim backgrounds."
    )
    parser.add_argument("image", help="Path to the input image")
    parser.add_argument(
        "-w",
        "--width",
        type=int,
        default=100,
        help="Output width in characters",
    )
    parser.add_argument("-o", "--output", help="Optional output text file")
    parser.add_argument(
        "--invert",
        choices=("auto", "yes", "no"),
        default="auto",
        help="Invert image polarity. Auto is best for light LaTeX pages.",
    )
    parser.add_argument(
        "--aspect-scale",
        type=float,
        default=0.45,
        help="Terminal character aspect compensation",
    )
    parser.add_argument(
        "--contrast",
        type=float,
        default=1.25,
        help="Final contrast multiplier",
    )
    parser.add_argument(
        "--contrast-cutoff",
        type=int,
        default=1,
        help="Autocontrast cutoff percentage",
    )
    parser.add_argument(
        "--chars",
        default=ASCII_CHARS,
        help="Characters ordered from darkest to brightest",
    )

    args = parser.parse_args()

    ascii_art = image_to_ascii(
        args.image,
        width=args.width,
        chars=args.chars,
        aspect_scale=args.aspect_scale,
        contrast_cutoff=args.contrast_cutoff,
        contrast=args.contrast,
        invert=args.invert,
    )

    if args.output:
        output = Path(args.output)
        output.write_text(ascii_art + "\n", encoding="utf-8")
    else:
        print(ascii_art)


if __name__ == "__main__":
    main()
