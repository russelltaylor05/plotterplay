from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom.minidom import parseString

def create_svg():
  svg_ns = "http://www.w3.org/2000/svg"
  inkscape_ns = "http://www.inkscape.org/namespaces/inkscape"
  svg = Element('svg', width="210mm", height="297mm", xmlns=svg_ns)

  square_size = 50
  grid_size = 2
  spacing = 5
  line_spacing = 5
  corner_radius = 3

  # Calculate total grid dimensions
  total_grid_width = grid_size * square_size + (grid_size - 1) * spacing
  total_grid_height = grid_size * square_size + (grid_size - 1) * spacing

  # Calculate offsets to center the grid
  page_width = 210  # in mm
  page_height = 297  # in mm
  offset_x = (page_width - total_grid_width) / 2
  offset_y = (page_height - total_grid_height) / 2

  group_black = SubElement(svg, 'g', id="2-black", attrib={"{http://www.inkscape.org/namespaces/inkscape}groupmode": "layer", "{http://www.inkscape.org/namespaces/inkscape}label": "2-black"})
  group_green = SubElement(svg, 'g', id="1-green", attrib={"{http://www.inkscape.org/namespaces/inkscape}groupmode": "layer", "{http://www.inkscape.org/namespaces/inkscape}label": "1-green"})

  for row in range(grid_size):
    for col in range(grid_size):
      x_position = offset_x + col * (square_size + spacing)
      y_position = offset_y + row * (square_size + spacing)
          
      rect = SubElement(group_black, 'rect', x=str(x_position), y=str(y_position), width=str(square_size), height=str(square_size), stroke="black", fill="none", rx=str(corner_radius), ry=str(corner_radius))
          
      # Add lines to fill the rectangle at 45 degrees
      for i in range(0, square_size + line_spacing, line_spacing):
          line = SubElement(group_green, 'line', x1=str(x_position), y1=str(y_position + i), x2=str(x_position + i), y2=str(y_position), stroke="#2ea44f", attrib={"stroke-width": "2"})
          if i != square_size:
              line = SubElement(group_green, 'line', x1=str(x_position + i), y1=str(y_position + square_size), x2=str(x_position + square_size), y2=str(y_position + i), stroke="#2ea44f", attrib={"stroke-width": "2"})
  
  # Convert to pretty XML string
  svg_string = tostring(svg)
  pretty_svg = parseString(svg_string).toprettyxml()

  # Save to file
  with open("grid.svg", "w") as f:
      f.write(pretty_svg)

create_svg()