import re

from services.base import HcBaseService


class HcDisplayService(HcBaseService):
    HYPR_SUNSET_CMD = "hyprsunset"
    HYPR_SUNSET_GAMMA_CMD = "gamma"
    HYPR_SUNSET_TEMP_CMD = "temperature"

    GAMMA_RANGE = (0, 100)
    TEMP_RANGE = (1000, 20000)

    def _run_sunset_cmd(self, *args: str) -> str:
        cmd = [
            self.HYPR_CTL_CMD,
            self.HYPR_SUNSET_CMD,
            *args,
        ]
        return self._run_cmd(cmd)

    def validate_operation(self, op: str) -> bool:
        return re.search("^(\\+|-)?\\d+$", op) is not None

    def validate_gamma(self, gamma: int) -> bool:
        return self.GAMMA_RANGE[0] <= gamma <= self.GAMMA_RANGE[1]

    def validate_temp(self, temp: int) -> bool:
        return self.TEMP_RANGE[0] <= temp <= self.TEMP_RANGE[1]

    def get_gamma(self) -> int:
        return int(self._run_sunset_cmd(self.HYPR_SUNSET_GAMMA_CMD))

    def set_gamma(self, value: int) -> None:
        self._run_sunset_cmd(self.HYPR_SUNSET_GAMMA_CMD, str(value))

    def get_temp(self) -> int:
        return int(self._run_sunset_cmd(self.HYPR_SUNSET_TEMP_CMD))

    def set_temp(self, value: int) -> None:
        self._run_sunset_cmd(self.HYPR_SUNSET_TEMP_CMD, str(value))
