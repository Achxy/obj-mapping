from ..helpers._checks import check_and_return


class Attribute:
    def __init__(
        self, *, mutable: bool = False, overwritable: bool = True, required: bool = True, not_required: bool = False
    ) -> None:
        self.mutable = check_and_return(mutable, bool)
        self.overwritable = check_and_return(overwritable, bool)
        self.required = check_and_return(required, bool)
        self.not_required = check_and_return(not_required, bool)
        if required and not_required:
            raise ValueError("required and not_required are mutually exclusive kwargs")
