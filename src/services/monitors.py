from typing import Optional

from services.base import HcBaseService


class HcMonitorService(HcBaseService):
    HYPR_CTL_MONITOR_KEY = "monitor"

    def turn_monitor_on(
        self,
        name: str,
        resolution: Optional[str] = None,
        position: Optional[str] = None,
        scale: Optional[float] = None,
    ) -> None:
        if resolution is None:
            resolution = "preferred"
        if position is None:
            position = "auto"
        if scale is None:
            scale = 1
        cmd = [
            self.HYPR_CTL_CMD,
            self.HYPR_CTL_KEYWORD_CMD,
            self.HYPR_CTL_MONITOR_KEY,
            f"{name},{resolution},{position},{scale}",
        ]
        self._run_cmd(cmd)

    def turn_monitor_off(self, name: str) -> None:
        cmd = [
            self.HYPR_CTL_CMD,
            self.HYPR_CTL_KEYWORD_CMD,
            self.HYPR_CTL_MONITOR_KEY,
            f"{name},disable",
        ]
        self._run_cmd(cmd)
