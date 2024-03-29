"""
Chord module.

"""

import re
from typing import List, Union

from FoxDot.lib.Patterns import PGroup, P
from FoxDot.lib.Patterns.Main import Pattern
from FoxDot.lib.Root import Note


class Chord(PGroup):
    """
    Musical chord to be manipulated by FoxDot

    The chord class generates chords that can be used by Foxdot.

    Examples:
        >>> chord = Chord('C#7/9')
        Chord("C#7/9")

    todos:
        - Adjust to `Root.default`
        - Accept chords with inverted bass, like: **(E/G#, Dm7/C)**
    """
    def __init__(self, chord: str):
        self.chord = chord
        super().__init__(self.notes)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f'Chord("{self.chord}")'

    def true_copy(self, new_data=None):
        new = self.__class__(self.chord)
        new.__dict__ = self.__dict__.copy()
        if new_data is not None:
            new.data = new_data
        return new

    def _get_note(self, pattern: str,  tons: int) -> Union[None, int, float]:
        if not re.search(pattern, self.chord):
            return None

        if self.is_flat:
            tons -= 1
        if self.is_sharp:
            tons += 1
        return self.tonic + tons

    @property
    def is_flat(self) -> bool:
        """
        Indicates whether the chord is flat

        Examples:
            >>> Chord('Cb').is_flat
            True
            >>> Chord('C#').is_flat
            False

        Returns:
            `True` if the chord is flat otherwise `False`
        """
        return bool(re.search(r'[-b]', self.chord))

    @property
    def is_sharp(self) -> bool:
        """
        Indicates whether the chord is sharp.

        Examples:
            >>> Chord('Cb').is_sharp
            False
            >>> Chord('C#').is_sharp
            True

        Returns:
            `True` if the chord is sharp otherwise `False`
        """
        return bool(re.search(r'[+#]', self.chord))

    @property
    def is_dim(self) -> bool:
        """
        Indicates whether the chord is sharp.

        Examples:
            >>> Chord('D').is_dim
            False
            >>> Chord('D⁰').is_dim
            True
            >>> Chord('D0').is_dim
            True
            >>> Chord('Do').is_dim
            True
            >>> Chord('DO').is_dim
            True
            >>> Chord('Ddim').is_dim
            True

        Returns:
            `True` if the chord is diminished otherwise `False`
        """
        return bool(re.search(r'([⁰0oO]|dim)', self.chord))

    @property
    def is_sus(self) -> bool:
        """
        Indicates whether the chord is suspended

        Examples:
            >>> Chord('Eb').is_sus
            False
            >>> Chord('Ebsus').is_sus
            True
            >>> Chord('Ebsus4').is_sus
            True
            >>> Chord('Eb4').is_sus
            True
            >>> Chord('Eb#3').is_sus
            True

        Returns:
            `True` if the chord is suspended otherwise `False`
        """
        return bool(re.search(r'(sus|4|#3)', self.chord))

    @property
    def is_minor(self) -> Union[bool, None]:
        """
        Indicates if the chord is minor.

        Examples:
            >>> Chord('E#').is_minor
            False
            >>> Chord('E#m').is_minor
            True
            >>> Chord('E#5').is_minor
            None

        Returns:
            (bool): `True` if the chord is minor otherwise `False`
            (None): If it is a power chord there is no way to know if it is
                minor, because it doesn't have the III of the chord
        """
        if self.is_power_chord:
            return
        return bool(re.search(r'^[A-G][b#]?m', self.chord))

    @property
    def is_power_chord(self) -> bool:
        """
        Indicates if the chord is minor.

        Examples:
            >>> Chord('E#').is_minor
            False

            >>> Chord('E#5').is_minor
            True

        Returns:
            `True` if it's a power chord otherwise `False`

        """
        return bool(re.search(r'^([A-G][b#]?5)$', self.chord))

    @property
    def notes(self) -> List[int]:
        """
        Chord notes.

        Examples:
            >>> Chord('C').notes
            [0, 2, 4]

        Returns:
            List of notes
        """
        degrees = [
            self.tonic,
            self.supertonic,
            self.third,
            self.subdominant,
            self.dominant,
            self.submediant,
            self.maj,
            self.ninth,
            self.eleventh,
            self.thirteenth,
        ]
        return list(filter(None, degrees))

    @property
    def tonic(self) -> int:
        """Tonic I."""
        if not (result := re.search(r'(^[A-G][b#]?)', self.chord)):
            raise Exception('Tonic inválid')
        return Note(result.group())  # + Root.default

    @property
    def supertonic(self):
        """Supertonic II."""
        return self._get_note(r'2', 2)

    @property
    def third(self):
        """Third III."""
        if self.is_power_chord:
            return None

        if self.is_dim or self.is_minor:
            return self.tonic + 3
        return self.tonic + 4

    @property
    def subdominant(self):
        """Subdominant IV."""
        if self.is_sus:
            return self.tonic + 5
        return self._get_note(r'4', 5)

    @property
    def dominant(self):
        """Dominant V."""
        if self.is_sus:
            return
        if self.is_dim or self.is_flat:
            return self.tonic + 6
        if self.is_sharp:
            return self.tonic + 8
        return self.tonic + 7

    @property
    def submediant(self):
        """Submediant VI."""
        return self._get_note(r'6', 9)

    @property
    def maj(self):
        """Maj VII."""
        if re.search(r'7(M|[Mm]aj)', self.chord):
            return self.tonic - 1
        if self.is_dim or re.search(r'7', self.chord):
            return self.tonic - 2

    @property
    def ninth(self):
        """Ninth IX."""
        return self._get_note(r'9', 2)

    @property
    def eleventh(self) -> int:
        """Eleventh XI."""
        return self._get_note(r'11', 5)

    @property
    def thirteenth(self) -> int:
        """Thirteenth XIII."""
        return self._get_note(r'13', 9)


class __chords__:
    """
    Creates a harmonic progression based on a list of chords.

    Parameters:
        chords (str): Many chords

    Examples:
        >>> PChord['Am7', 'C(7/9)', 'F7Maj', 'G(4/9/13)']  # Djavan - Mal de Mim
        P[Chord("Am7"), Chord("C(7/9)"), Chord("F7Maj"), Chord("G4/9/13")]

    Returns:
        (FoxDot.lib.Patterns.Main.Pattern[Chord]): A `Chord` pattern.
            For more details about the `Pattern` object see the
            [FoxDot documentation](https://foxdot.org/docs/pattern-basics/)

    """
    def __getitem__(self, chords) -> Pattern:
        chords = [Chord(chord) for chord in chords]
        return P[chords]


PChord = __chords__()
