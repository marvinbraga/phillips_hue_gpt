class PromptInstructionsHue:
    @staticmethod
    def get():
        return """ 
        I have the following list of light bulbs and I want you to create a color configuration for
         them that make up a theme according to the following instructions:

        <<INSTRUCTIONS>> 
        {text}

        <<LIST OF LAMPS AND RELATED INFORMATION>>
        Here is the list of my lamps with their respective placements:

        The ceiling has a height of approximately 2.3 meters.

        Lâmpada 1: Ceiling, left lamp, right position. 
        Lâmpada 2: Ceiling, left lamp, left position. 
        Lâmpada 3: Ceiling, right lamp, left position. 
        Lâmpada 4: Ceiling, right lamp, right position.

        Hue Iris: Table on my right side, height of 65cm.

        Hue Play 1: Behind my main monitor on the left side. 
        Hue Play 2: Behind my main monitor on the right side.

        Fita Led: In front of me and behind my table at 20cm, behind my main monitor, 
        75cm off the ground.

        Led cima: In front of me, 20cm behind my main monitor, 1.50cm off the ground.

        <<OUTPUT FILE INFORMATION>>
        You should create a JSON file structure with the following information:

        name: The name of the setting. This is a unique identifier for the setting. Create a name 
        that makes sense with the colors that make up the setting. The name should be in English 
        and if there are white spaces then change them to underscore.

        description: A brief description of the setting. This can include details about the 
        environment in which the setting is used.

        settings: A list of light settings. 
        Each light setting should include:

        light_name: The name of the light or lamp.
        color: The color of the light. This should be a dictionary with the following fields: 
          red: The intensity of the red (between 0 and 255). 
          green: The intensity of the green (between 0 and 255). 
          blue: The intensity of the blue (between 0 and 255). 
          brightness: The brightness of the light (between 0 and 255).

        <<EXAMPLE OF JSON FILE>>
        Here is an example of how you can create a new light setting:

        Here are the details extracted:

        name: The 'name' key represents the name given for the current lighting system 
        configuration, which in this case is 'your_new_configuration'.
        description: The 'description' key provides a detailed description of the environment 
        and lights, which helps understand the purpose and context of the setting.
        settings: The 'settings' key is a list that contains the settings of each light bulb 
        or lamp that is part of the lighting system. Each item in this list is an object that 
        contains two keys: 'light_name' and 'color'.
        light_name: The 'light_name' key is the name given to the light bulb or lamp. You should 
        use the exact names provided in these instructions, in the list of lamps.
        color: The 'color' key is an object that contains the color information and brightness 
        for the light. The colors are represented by three keys: 
        'red', 'green', and 'blue', which follow the RGB color model. 
        The 'brightness' key determines the brightness level of the light. In the provided 
        example, both lights have the color set to white (255,255,255 in the RGB model) and the 
        brightness set to 100.

        To add more lamp settings, you can simply add more objects to the 'settings' list. 
        Each object should contain the keys 'light_name' and 'color' with their respective 
        information.

        Replace "your_new_configuration", "A detailed description of the environment and lights", 
        "Name of your light bulb or lamp 1" and "Name of your light bulb or lamp 2" with the 
        desired values. Adjust the values of red, green, blue, and brightness to achieve the 
        desired color and brightness for each light.

        <<ANSWER OUTPUT>> 
        Format the output as JSON and its respective keys and values. Just this. 
        """


class PromptResponseHue:
    @staticmethod
    def get(lang="Português do Brasil"):
        return f"""
        Please clearly explain why you chose this color configuration for this instruction.
        
        <<INSTRUCTIONS>> 
        {{instructions}}
        
        <<CONFIGURATION>>
        ```json
        {{text}}
        ```
        
        <<OUTPUT>>
        Always translate your answer to this language: {lang}.
        """
