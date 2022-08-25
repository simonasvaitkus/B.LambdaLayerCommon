import re
from datetime import datetime
from typing import Any


class ValueValidator:
    def __init__(self, value: Any):
        self.__value = value

    @property
    def value(self):
        return self.__value

    def not_null(self) -> 'ValueValidator':
        if self.__value is None:
            raise ValueError(f'Value "{self.__value}" can not be null.')
        return self

    def is_str(self) -> 'ValueValidator':
        if not isinstance(self.__value, str):
            raise ValueError(f'Value "{self.__value}" must be string.')
        return self

    def is_int(self) -> 'ValueValidator':
        if not isinstance(self.__value, int):
            raise ValueError(f'Value "{self.__value}" must be integer.')
        return self

    def not_empty(self) -> 'ValueValidator':
        self.is_iterable()
        if len(self.__value) == 0:
            raise ValueError(f'Value "{self.__value}" must not be empty.')
        return self

    def min_len(self, length: int) -> 'ValueValidator':
        self.is_iterable()
        if len(self.__value) < length:
            raise ValueError(f'Value "{self.__value}" must be longer than {length}.')
        return self

    def max_len(self, length: int) -> 'ValueValidator':
        self.is_iterable()
        if len(self.__value) > length:
            raise ValueError(f'Value "{self.__value}" must be shorter than {length}.')
        return self

    def is_country_iso2(self) -> 'ValueValidator':
        self.is_iterable()
        if len(self.__value) != 2:
            raise ValueError(f'Value "{self.__value}" is not country ISO2.')
        return self

    def is_country_iso3(self) -> 'ValueValidator':
        self.is_iterable()
        if len(self.__value) != 3:
            raise ValueError(f'Value "{self.__value}" is not country ISO3.')
        return self

    def is_str_date(self) -> 'ValueValidator':
        try:
            datetime.fromisoformat(self.__value)
        except (ValueError, TypeError):
            raise ValueError(f'Value "{self.__value}" is not ISO date.')
        return self

    def is_email(self) -> 'ValueValidator':
        self.is_str()
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.fullmatch(regex, self.__value):
            raise ValueError(f'Value "{self.__value}" is not an email.')
        return self

    def min_number(self, number: int) -> 'ValueValidator':
        self.is_int()
        if self.__value < number:
            raise ValueError(f'Value "{self.__value}" is bigger than {number}.')
        return self

    def max_number(self, number: int) -> 'ValueValidator':
        self.is_int()
        if self.__value > number:
            raise ValueError(f'Value "{self.__value}" is smaller than {number}.')
        return self

    def is_list(self) -> 'ValueValidator':
        if not isinstance(self.__value, list):
            raise ValueError(f'Value "{self.__value}" is not a list.')
        return self

    def is_list_of_strings(self) -> 'ValueValidator':
        self.is_list()
        if not all([isinstance(item, str) for item in self.__value]):
            raise ValueError(f'Value "{self.__value}" is not a list of strings.')
        return self

    def is_alphanumeric(self) -> 'ValueValidator':
        self.is_str()
        if not self.__value.isalnum():
            raise ValueError(f'Value "{self.__value}" is not alphanumeric.')
        return self

    def alpha_only(self) -> 'ValueValidator':
        self.is_str()
        if not self.__value.isalpha():
            raise ValueError(f'Value "{self.__value}" should contain only alpha characters.')
        return self

    def is_iterable(self) -> 'ValueValidator':
        self.not_null()
        try:
            iter(self.__value)
        except TypeError:
            raise ValueError(f'Value "{self.__value}" is not iterable.')
        return self

    def contains_lowercase(self) -> 'ValueValidator':
        self.is_str()
        if not any([char.islower() for char in self.__value]):
            raise ValueError(f'Value "{self.__value}" does not contain lowercase characters.')
        return self

    def contains_uppercase(self):
        self.is_str()
        if not any([char.isupper() for char in self.__value]):
            raise ValueError(f'Value "{self.__value}" does not contain uppercase characters.')
        return self

    def contains_digit(self):
        self.is_str()
        if not any([char.isdigit() for char in self.__value]):
            raise ValueError(f'Value "{self.__value}" does not contain digits.')
        return self

    def contains_special(self):
        self.is_str()
        if not any([not char.isalnum() for char in self.__value]):
            raise ValueError(f'Value "{self.__value}" does not contain special characters.')
        return self