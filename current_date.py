import datetime
from typing import Any

from langchain_core.tools import BaseTool

class CurrentDateTool(BaseTool):
    name: str = "current_date"
    description :str = "Return the current date in /DD/MM/YYYY format"

    def _run(self):
        "Synchronous current date lookup"
        now = datetime.datetime.now()
        return now.strftime("%d/%m/%Y")

    def _arun(self):
        "ASynchronous current date lookup"
        now = datetime.datetime.now()
        return now.strftime("%d/%m/%‚Y")