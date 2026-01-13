import subprocess


class HcBaseService:
    HYPR_CTL_CMD = "hyprctl"
    HYPR_CTL_KEYWORD_CMD = "keyword"

    def _run_cmd(self, cmd: list[str]) -> str:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()
