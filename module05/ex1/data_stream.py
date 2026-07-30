
from abc import ABC, abstractmethod
from typing import Any


class NoValidation(Exception):

    def __init__(self, message="Improper data") -> None:
        super().__init__(message)


class DataProcessor(ABC):

    def __init__(self) -> None:
        self._storage: list = []
        self._out_calls: int = 0
        self._ingestions: int = 0
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


class DataStream():

    def __init__(self) -> None:
        self._processors: list[Any] = []

    def register_processor(self, proc: DataProcessor) -> None:

        for processor in self._processors:
            if proc.__class__ == type(processor):
                print(f"Registering Processor failed. \
Theres already a {processor.__class__.__name__}")
                return
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:

        for item in stream:
            item_ingest: bool = False
            for processor in self._processors:
                if processor.validate(item):
                    processor.ingest(item)
                    item_ingest = True
                    break
            if not item_ingest:
                print(f"DataStream error - \
Can't Process element in stream: {item}")

    def print_processors_stats(self) -> None:

        print("=== DataStream Statistics ===")
        if not self._processors:
            print("No processor found, no data")
        else:
            for processor in self._processors:
                print(f"{processor.__class__.__name__}: \
total {processor._ingestions}, \
remaining {len(processor._storage)}")


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
                self._ingestions += 1
            elif isinstance(data, list):
                self._storage.extend([str(item) for item in data])
                self._ingestions += len(data)


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
                self._ingestions += 1
            else:
                self._storage.extend(data)
                self._ingestions += len(data)


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
                self._ingestions += 1
            elif isinstance(data, list):
                for dic in data:
                    dic_str: str = ": ".join(dic.values())
                    self._storage.append(dic_str)
                self._ingestions += len(data)


def main() -> None:

    data: list = [
        'ola',
        43,
        ['adeus', 'andre'],
        [1, 2, 3, 4],
        [
            {
                'log_level': 'WARNING',
                ' log_message': 'Telnet access! Use ssh instead'
            },
            {
                'log_level': 'INFO',
                'log_message': 'User wil is connected'
            }
        ],
        {
            'log_level': 'NOTICE',
            'log_message': 'Connection to server'
        },
    ]
    print("=== Code Nexus - Data Stream ===")
    DataStreamer: DataStream = DataStream()
    print("Initialized Data Stream...")
    DataStreamer.print_processors_stats()
    print("\nRegistering Numeric Processor")
    DataStreamer.register_processor(NumericProcessor())
    print(f"Sending first batch of data: {data}\n")
    DataStreamer.process_stream(data)
    print()
    DataStreamer.print_processors_stats()
    print("\nRegistering other data processors")
    DataStreamer.register_processor(TextProcessor())
    DataStreamer.register_processor(LogProcessor())
    print("Sending the same data again...\n")
    DataStreamer.process_stream(data)
    DataStreamer.print_processors_stats()
    print("\nattempting to add a new processor that already exists...\n")
    DataStreamer.register_processor(NumericProcessor())
    print("\nConsuming some processor elements:")
    for processor in DataStreamer._processors:
        print(f"{processor.__class__.__name__} \
{processor.output()}, {processor.output()}")
    print()
    DataStreamer.print_processors_stats()


if __name__ == "__main__":
    main()
