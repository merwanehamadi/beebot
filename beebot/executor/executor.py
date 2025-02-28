import json
import logging
from typing import TYPE_CHECKING

from pydantic import ValidationError

from beebot.models import Decision
from beebot.models.observation import Observation

if TYPE_CHECKING:
    from beebot.body import Body

logger = logging.getLogger(__name__)


class Executor:
    body: "Body"

    def __init__(self, body: "Body"):
        self.body = body

    def execute(self, decision: Decision) -> Observation:
        """Get pack from tool name. call it"""
        pack = self.body.packs.get(decision.tool_name)
        if not pack:
            return Observation(
                success=False,
                error_reason=f"Invalid tool name received: {decision.tool_name}. It may be invalid or may not be "
                f"installed.",
            )

        tool_args = decision.tool_args or {}
        try:
            result = pack.run(**tool_args)
            return Observation(response=result)
        except ValidationError as e:
            logger.error(f"Error on execution: {e}")
            return Observation(response=f"Error: {json.dumps(e.errors())}")
        except Exception as e:
            logger.error(f"Error on execution: {e}")
            return Observation(response=f"Exception: {e}")
