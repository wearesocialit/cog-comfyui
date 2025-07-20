from custom_node_helper import CustomNodeHelper
import os

IPADAPTERS = [
    "ip-adapter.bin",
]

class ComfyUI_IPAdapter_Flux(CustomNodeHelper):
    @staticmethod
    def prepare(**kwargs):
        # create the ipadapter folder in ComfyUI/models/ipadapter
        # if it doesn't exist at setup time then the plugin defers to the base directory
        # and won't look for our ipadaters that are downloaded on demand
        if not os.path.exists("ComfyUI/models/ipadapter-flux"):
            os.makedirs("ComfyUI/models/ipadapter-flux")

    @staticmethod
    def models():
        return IPADAPTERS

    @staticmethod
    def weights_map(base_url):
        ipadapter_map = {
            model: {
                "url": f"{base_url}/ipadapter-flux/{model}.tar",
                "dest": "ComfyUI/models/ipadapter-flux/",
            }
            for model in IPADAPTERS
        }
        return {**ipadapter_map}
