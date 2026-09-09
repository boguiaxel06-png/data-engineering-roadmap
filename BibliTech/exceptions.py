class ISBNInvalideError(Exception):
    """ Exception lévée si un ISBN ne respecte pas le format ou est vide """
    pass


class DocumentNonTrouveError:
    """ Exception lévée si un document cherché n' existe pas dans une médiathèque """
    pass
