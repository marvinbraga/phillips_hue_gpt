from phue import Bridge, Light

from marvin_hue.basics import LightConfig
from marvin_hue.colors import Color
from marvin_hue.utils import RGBtoXYAdapter


class HueController:
    """
    Classe para controlar as lâmpadas Philips Hue.
    Esta classe utiliza a ponte de Hue para interagir com as lâmpadas e permite definir a cor das lâmpadas,
    aplicar configurações de luz e listar grupos e lâmpadas.

    Args:
        ip_address (str): O endereço IP da ponte Hue.

    Attributes:
        bridge (Bridge): A ponte Hue para interagir com as lâmpadas.
        lights (list): A lista de objetos de luz acessíveis através da ponte.
    """

    def __init__(self, ip_address):
        """
        Inicializa a ponte Hue e obtém a lista de lâmpadas.
        """

        self.bridge = Bridge(ip_address)
        self.bridge.connect()
        self.lights = self.bridge.get_light_objects()

    def set_light_color(self, light_name, color: Color) -> Light:
        """
        Define a cor da lâmpada especificada.

        Args:
            light_name (str): O nome da lâmpada.
            color (Color): O objeto de cor RGB para definir a lâmpada.

        Returns:
            Light: O objeto de luz com a cor definida.
        """

        xy = RGBtoXYAdapter.convert(color.red, color.green, color.blue)
        light = self._get_light_by_name(light_name)
        light.xy = xy
        light.brightness = color.brightness
        return light

    def apply_light_config(self, light_config: LightConfig, transition_time_secs=0):
        """
        Aplica uma configuração de luz às lâmpadas.

        Args:
            light_config (LightConfig): A configuração de luz a ser aplicada.
            transition_time_secs (int, optional): O tempo de transição em segundos. Padrão para 0.

        Returns:
            HueController: A instância de controlador Hue atual.
        """

        for setting in light_config.settings:
            light = self.set_light_color(setting.light_name, setting.color)
            if transition_time_secs:
                light.transitiontime = transition_time_secs * 10
                light.on = True
        return self

    def _get_light_by_name(self, light_name):
        """
        Obtém uma lâmpada pelo nome.

        Args:
            light_name (str): O nome da lâmpada.

        Returns:
            Light: O objeto de luz correspondente ao nome, ou None, se não for encontrado.
        """

        return next((light for light in self.lights if light.name == light_name), None)

    def list_groups(self):
        """
        Lista todos os grupos de lâmpadas.

        Returns:
            list: Uma lista de tuplas com o ID e o nome do grupo.
        """

        groups = self.bridge.groups
        return [(group.group_id, group.name) for group in groups]

    def list_lights(self):
        """
        Lista todos as lâmpadas.

        Returns:
            list: A lista de nomes de lâmpadas.
        """

        return [light.name for light in self.lights]
