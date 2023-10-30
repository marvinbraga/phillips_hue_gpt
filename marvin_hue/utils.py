class RGBtoXYAdapter:
    """
    Esta classe, RGBtoXYAdapter, atua como uma interface para a conversão de cores do sistema
    RGB (vermelho, verde e azul), comumente utilizado em computadores, para o espaço de cores XY.
    O método interno `convert` realiza ajustes nos valores RGB para otimizar a compreensão e
    manipulação das cores. Posteriormente, realiza cálculos para transformar esses valores ajustados
    em novos valores X, Y e Z. Com esses valores, são realizados cálculos adicionais para determinar
    x e y, que representam a cor no espaço de cores XY. Este sistema de cores é amplamente utilizado
    em lâmpadas inteligentes, como as Philips Hue, por representar cores de maneira mais fiel à
    percepção humana e por ser energeticamente eficiente para luzes de LED. A implementação desta
    classe, portanto, facilita a conversão de cores para compatibilidade com tais dispositivos.
    """
    @staticmethod
    def check_min_max(value):
        result = value if value > 0 else 0
        result = result if result < 256 else 255
        return result

    @staticmethod
    def convert(red: int, green: int, blue: int) -> (float, float):
        red = RGBtoXYAdapter.check_min_max(red)
        green = RGBtoXYAdapter.check_min_max(green)
        blue = RGBtoXYAdapter.check_min_max(blue)
        if red + green + blue == 0:
            blue = 1

        red = ((red + 0.055) / (1.0 + 0.055)) ** 2.4 if red > 0.04045 else red / 12.92
        green = ((green + 0.055) / (1.0 + 0.055)) ** 2.4 if green > 0.04045 else green / 12.92
        blue = ((blue + 0.055) / (1.0 + 0.055)) ** 2.4 if blue > 0.04045 else blue / 12.92

        X = red * 0.664511 + green * 0.154324 + blue * 0.162028
        Y = red * 0.283881 + green * 0.668433 + blue * 0.047685
        Z = red * 0.000088 + green * 0.072310 + blue * 0.986039

        x = X / (X + Y + Z)
        y = Y / (X + Y + Z)
        return x, y
