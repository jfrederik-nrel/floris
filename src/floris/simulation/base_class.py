# Copyright 2021 NREL

# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

# See https://floris.readthedocs.io for documentation


"""
Defines the BaseClass parent class for all models to be based upon.
"""

from abc import ABC, abstractmethod, abstractstaticmethod
from typing import Any, Dict

import attr
from floris.utilities import FromDictMixin
from floris.logging_manager import LoggerBase


@attr.s(auto_attribs=True)
class BaseClass(LoggerBase, FromDictMixin):
    """
    BaseClass object class. This class does the logging and MixIn class inheritance so
    that it can't be overlooked in creating new models.
    """

    @classmethod
    def get_model_defaults(cls) -> Dict[str, Any]:
        """Produces a dictionary of the keyword arguments and their defaults.

        Returns
        -------
        Dict[str, Any]
            Dictionary of keyword argument: default.
        """
        return {el.name: el.default for el in attr.fields(cls)}

    def _get_model_dict(self) -> dict:
        """Convenience method that wraps the `attr.asdict` method. Returns the model's
        parameters as a dictionary.

        Returns
        -------
        dict
            The provided or default, if no input provided, model settings as a dictionary.
        """
        return attr.asdict(self)


@attr.s(auto_attribs=True)
class BaseModel(BaseClass, ABC):

    model_string: str = attr.ib(default=None, kw_only=True)

    def __attrs_post_init__(self) -> None:
        if self.model_string is None:
            raise ValueError("No 'model_string' defined.")

    @abstractmethod
    def prepare_function() -> None:
        raise NotImplementedError("BaseModel.prepare_function")

    @abstractmethod
    def function() -> None:
        raise NotImplementedError("BaseModel.function")
