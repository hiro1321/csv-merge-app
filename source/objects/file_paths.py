from dataclasses import dataclass


@dataclass
class FilePaths:
    input_file1_path: str
    input_file2_path: str
    output_directory: str

    def __init__(
        self,
        input_file1_path: str = "",
        input_file2_path: str = "",
        output_directory: str = "",
    ):
        self.input_file1_path = input_file1_path
        self.input_file2_path = input_file2_path
        self.output_directory = output_directory

    def validate(self):
        return (
            self.input_file1_path != ""
            and self.input_file2_path != ""
            and self.output_directory != ""
        )
