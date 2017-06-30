# GDquest-VSE

Video editing add-on for Blender

Blender's video editor has a lot of potential, but it lacks some essential tools for content creators. I produced [hundreds of tutorials](http://youtube.com/c/gdquest) since 2015, and work exclusively with Blender.

Here are the tools I built to edit tutorials faster.

## Heavy Work in Progress

The tools themselves work, but the add-on is not documented yet, and not ready for everyone to use. You'll have to assign the operators to shortcuts by yourself, or you could use [this keymap](https://gist.github.com/NathanLovato/84b3a8529e5757875c8e97f4d7b424f4).

## Other add-ons

Here are other recommended add-ons for a better editing workflow:

1. [VSE transform tools](https://github.com/kgeogeo/VSE_Transform_Tools): Move and animate transform effects visually, on the image preview area
2. [Easy logging](http://www.easy-logging.net/): Adds tools to derush and tag footage


# Available tools

## Mouse-based editing tools

### Trim

## Import and export

### Import local footage

Import videos, audio and pictures sitting around the .blend project file with a single keystroke! You do need to put the files in subfolders named:

1. audio for the audio files (.wav, etc.)
2. img for the pictures (.png, etc.)
3. video for the video clips (.mp4, .mkv, etc.)

The VSE tools will find all the valid files in your project subfolders and import them to the sequencer.