###
### Module that handles theming
### 

import sys
import json 

if sys.version_info.major == 3:
    import tkinter as tk, tkinter.font as tk_font
else:
    import TKinter as tk, tkFont as tk_font

class ThemeManager:
    # Default heading font size (pt)
    HEADING_FT_SIZE_NORMAL_DEFAULT = 16
    HEADING_FT_SIZE_LARGE_DEFAULT = 18
    HEADING_FT_SIZE_SMALL_DEFAULT = 15

    # Default heading weights
    HEADING_WEIGHT_NORMAL_DEFAULT = 'normal'
    HEADING_WEIGHT_THICK_DEFAULT = 'thick'
    HEADING_WEIGHT_THIN_DEFAULT = "thin"

    # Default heading font family
    HEADING_FT_FAMILY_DEFAULT = 'helvetica'

    # Default Paragraph font size
    PARAGRAPH_FT_SIZE_NORMAL_DEFAULT = 13
    PARAGRAPH_FT_SIZE_LARGE_DEFAULT = 14
    PARAGRAPH_FT_SIZE_SMALL_DEFAULT = 12

    PARAGRAPH_FT_FAMILY_DEFAULT = 'helvetica'

    # Default background colors
    BG_COLOR_NORMAL_DEFAULT = '#222222'
    BG_COLOR_DARK_DEFAULT = '#111111'
    BG_COLOR_LIGHT_DEFAULT = '#333333'

    # Default text colors
    TXT_COLOR_NORMAL_DEFAULT = '#222222'
    TXT_COLOR_DARK_DEFAULT = '#111111'
    TXT_COLOR_LIGHT_DEFAULT = '#333333'

    # Default separator colors
    SEPARATOR_COLOR_DEFAULT = '#222222'

    def __init__(self):
        self.heading_ft_size_normal = self.HEADING_FT_SIZE_NORMAL_DEFAULT
        self.heading_ft_size_large = self.HEADING_FT_SIZE_LARGE_DEFAULT
        self.heading_ft_size_small = self.HEADING_FT_SIZE_SMALL_DEFAULT

        self.heading_weight_normal = self.HEADING_WEIGHT_NORMAL_DEFAULT
        self.heading_weight_thick = self.HEADING_WEIGHT_THICK_DEFAULT
        self.heading_weight_thin = self.HEADING_WEIGHT_THIN_DEFAULT

        self.heading_ft_family = self.HEADING_FT_FAMILY_DEFAULT

        self.paragraph_ft_size_normal = self.PARAGRAPH_FT_SIZE_NORMAL_DEFAULT
        self.paragraph_ft_size_large = self.PARAGRAPH_FT_SIZE_LARGE_DEFAULT
        self.paragraph_ft_size_small = self.PARAGRAPH_FT_SIZE_SMALL_DEFAULT

        self.paragraph_ft_family = self.PARAGRAPH_FT_FAMILY_DEFAULT

        self.bg_color_normal = self.BG_COLOR_NORMAL_DEFAULT
        self.bg_color_dark = self.BG_COLOR_DARK_DEFAULT
        self.bg_color_light = self.BG_COLOR_LIGHT_DEFAULT

        self.txt_color_normal = self.TXT_COLOR_NORMAL_DEFAULT
        self.txt_color_dark = self.TXT_COLOR_DARK_DEFAULT
        self.txt_color_light = self.TXT_COLOR_LIGHT_DEFAULT

        self.separator_color = self.SEPARATOR_COLOR_DEFAULT

        # Named font objects to be generated from 
        # the theme
        self.nf_heading_normal = None
        self.nf_heading_large = None
        self.nf_heading_small = None

        self.nf_paragraph_normal = None
        self.nf_paragraph_large = None
        self.nf_paragraph_small = None

        self.configure_fonts()

    def load_theme(self, theme_file: str):
        '''
        Loads and parses the provided theme file and store the theme settings.
        The stored theme settings are used by the application widgets to change
        how they look.

        param:
            theme_file - Path to theme file which should be in json format
        '''

        with open(theme_file, 'r') as theme_file_obj:
            theme_file_contents = json.load(theme_file_obj)

        # Headings
        self.heading_ft_size_normal = theme_file_contents['heading_ft_size_normal']
        self.heading_ft_size_large = theme_file_contents['heading_ft_size_large']
        self.heading_ft_size_small = theme_file_contents['heading_ft_size_small']

        self.heading_weight_normal = theme_file_contents['heading_weight_normal']
        self.heading_weight_thick = theme_file_contents['heading_weight_thick']
        self.heading_weight_thin = theme_file_contents['heading_weight_thin']

        self.heading_ft_family = theme_file_contents['heading_ft_family']

        # Paragraphs
        self.paragraph_ft_size_normal = theme_file_contents['paragraph_ft_size_normal']
        self.paragraph_ft_size_large = theme_file_contents['paragraph_ft_size_large']
        self.paragraph_ft_size_small = theme_file_contents['paragraph_ft_size_small']

        self.paragraph_ft_family = theme_file_contents['paragraph_ft_family']

        # Colors
        self.bg_color_normal = theme_file_contents['bg_color_normal']
        self.bg_color_dark = theme_file_contents['bg_color_dark']
        self.bg_color_light = theme_file_contents['bg_color_light']

        self.txt_color_normal = theme_file_contents['txt_color_normal']
        self.txt_color_dark = theme_file_contents['txt_color_dark']
        self.txt_color_light = theme_file_contents['txt_color_light']

        self.separator_color = theme_file_contents['separator_color']

        self.configure_fonts()

    def configure_fonts(self):
        '''
        Takes all theme settings and creates named font objects that can be used
        throughout the application widgets.
        '''

        self.nf_heading_normal = tk_font.Font(family=self.heading_ft_family, size=self.heading_ft_size_normal)
        self.nf_heading_large = tk_font.Font(family=self.heading_ft_family, size=self.heading_ft_size_large)
        self.nf_heading_small = tk_font.Font(family=self.heading_ft_family, size=self.heading_ft_size_small)

        self.nf_paragraph_normal = tk_font.Font(family=self.paragraph_ft_family, size=self.paragraph_ft_size_normal)
        self.nf_paragraph_large = tk_font.Font(family=self.paragraph_ft_family, size=self.paragraph_ft_size_large)
        self.nf_paragraph_small = tk_font.Font(family=self.paragraph_ft_family, size=self.paragraph_ft_size_small)





