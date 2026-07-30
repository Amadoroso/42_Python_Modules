
from typing import Any
from abc import ABC, abstractmethod


class NoValidation(Exception):

    def __init__(self, message="Improper data") -> None:
        super().__init__(message)


class DataProcessor(ABC):

    def __init__(self) -> None:
        self._storage: list = []
        self._out_calls: int = 0
        super().__init__()

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:

        if not self._storage:
            raise IndexError
        out_tuple: tuple[int, str] = (
            self._out_calls, self._storage.pop(0)
            )
        self._out_calls += 1
        return out_tuple


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:

        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            for x in data:
                if not isinstance(x, (int, float)):
                    return False
            return True
        else:
            return False

    def ingest(self, data: int | float | list) -> None:

        if not self.validate(data):
            raise NoValidation("Improper Numeric data")
        else:
            if isinstance(data, (int, float)):
                self._storage.append(str(data))
            elif isinstance(data, list):
                self._storage.extend([str(item) for item in data])


class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:

        if isinstance(data, str):
            return True
        if isinstance(data, list):
            for x in data:
                if not isinstance(x, str):
                    return False
            return True
        else:
            return False

    def ingest(self, data: str | list[str]) -> None:

        if not self.validate(data):
            raise NoValidation("Improper Text data")
        else:
            if isinstance(data, str):
                self._storage.append(data)
            else:
                self._storage.extend(data)


class LogProcessor(DataProcessor):

    @staticmethod
    def __is_valid_dict(dictio: dict[Any, Any]):

        if not isinstance(dictio, dict):
            return False

        for key, value in dictio.items():
            if not isinstance(key, str):
                return False
            if not isinstance(value, str):
                return False
        return True

    def validate(self, data: Any) -> bool:

        if isinstance(data, dict):
            return self.__is_valid_dict(data)
        elif isinstance(data, list):
            for dictio in data:
                if not self.__is_valid_dict(dictio):
                    return False
            return True
        else:
            return False

    def ingest(self, data: dict | list[dict]) -> None:

        if not self.validate(data):
            raise NoValidation("Improper Log data")
        else:
            if isinstance(data, dict):
                data_str: str = ": ".join(data.values())
                self._storage.append(data_str)
            elif isinstance(data, list):
                for dic in data:
                    dic_str: str = ": ".join(dic.values())
                    self._storage.append(dic_str)


def numeric_tester() -> None:

    print("Testing Numeric Processor...")
    NumProc: NumericProcessor = NumericProcessor()
    print(f"Validating '456': {NumProc.validate(456)}")
    print(f"Validating 'ADEUS': {NumProc.validate('ADEUS')}")
    try:
        print("Testing invalid ingestion of 'OLA':", end=" ")
        NumProc.ingest('OLA')  # type: ignore
    except NoValidation as e:
        print(e)
    try:
        print("Testing invalid ingestion of [1, 2, 'ola']:", end=" ")
        NumProc.ingest([1, 2, 'ola'])  # type: ignore
    except NoValidation as e:
        print(e)
    print("ingesting: 1, 2, 3 and [4, 5, 6]")
    NumProc.ingest(1)
    NumProc.ingest(2)
    NumProc.ingest(3)
    NumProc.ingest([4, 5, 6])
    print("Extracting everything...")
    for x in range(7):
        try:
            out_tuple: tuple[int, str] = NumProc.output()
            print(f"Value {out_tuple[0]}: {out_tuple[1]}")
        except IndexError:
            print("IndexError: NumProc is empty!")


def text_tester() -> None:

    print("\nTesting Text Processor...")
    TextProc: TextProcessor = TextProcessor()
    print(f"Validating '456': {TextProc.validate(456)}")
    print(f"Validating 'ADEUS': {TextProc.validate('ADEUS')}")
    try:
        print("Testing invalid ingestion of '3456':", end=" ")
        TextProc.ingest(3456)  # type: ignore
    except NoValidation as e:
        print(e)
    try:
        print("Testing invalid ingestion of ['ola', 'adeus', 3]:", end=" ")
        TextProc.ingest(['ola', 'adeus', 3])  # type: ignore
    except NoValidation as e:
        print(e)
    print("ingesting: 'a', 'b', 'ola' and ['4', '5', '6']")
    TextProc.ingest('a')
    TextProc.ingest('b')
    TextProc.ingest('ola')
    TextProc.ingest(['4', '5', '6'])
    print("Extracting everything...")
    for x in range(7):
        try:
            out_tuple: tuple[int, str] = TextProc.output()
            print(f"Value {out_tuple[0]}: {out_tuple[1]}")
        except IndexError:
            print("IndexError: TextProc is empty!")


def log_tester() -> None:

    print("\nTesting Log Processor...")
    LogProc: LogProcessor = LogProcessor()
    print(f"Validating '456': {LogProc.validate(456)}")
    print(f"Validating 'ADEUS': {LogProc.validate('ADEUS')}")
    dic: dict = {
        'log_level': 'NOTICE',
        'log_message': 'Connection to server'
        }
    print(f"Validating {dic}: {LogProc.validate(dic)}")
    try:
        print("Testing invalid ingestion of '3456':", end=" ")
        LogProc.ingest(3456)  # type: ignore
    except NoValidation as e:
        print(e)
    try:
        print(f"Testing invalid ingestion of {[dic, 4]}:", end=" ")
        LogProc.ingest([dic, 4])  # type: ignore
    except NoValidation as e:
        print(e)
    lst_dic: list[dict] = [
        {
            'log_level': 'ERROR',
            'log_message': 'Unauthorized access!!'
        },
        {
            'log_level': 'NOTICE',
            'log_message': 'Unable connect'
        }
    ]
    print(f"ingesting: {dic} and {lst_dic}")
    LogProc.ingest(dic)
    LogProc.ingest(lst_dic)
    print("Extracting everything...")
    for x in range(4):
        try:
            out_tuple: tuple[int, str] = LogProc.output()
            print(f"Value {out_tuple[0]}: {out_tuple[1]}")
        except IndexError:
            print("IndexError: LogProc is empty!")


def main() -> None:

    print("=== Code Nexus - Data Processor ===\n")
    numeric_tester()
    text_tester()
    log_tester()


if __name__ == "__main__":
    main()
