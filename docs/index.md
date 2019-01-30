# Hex Team Color Codes to RGB
A simple python script to convert Hex color codes into RGB. It's what I used on [https://usteamcolors.com](https://usteamcolors.com) to get the RGB values for the team color codes.

## Usage
This is a very simple function that will take a Hex color code as parameter and will return the corresponding RGB values, each separated by a space.

First, you'll want to import the function into your own script

```python
from hex2rgb import hex2rgb
```

Then you simply call the function not forgetting to add the Hex color as a parameter. A you print the result

```python
print hex2rgb('#4E2683')
```

This should return `78 38 131`. And those are the RGB values.
