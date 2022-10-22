from manim import *
from random import randint

presenter = "First Last"
font = "Menlo"

class CodingClubPersonScreenSaver(Scene):
    def construct(self):
        firstStringSequence, secondStringSequence, \
        thirdStringSequence, fourthStringSequence, \
        = "", "", "", ""

        for i in range(5):
            firstStringSequence += str(randint(0, 1))
        for i in range(5):
            secondStringSequence += str(randint(0, 1))
        for i in range(5):
            thirdStringSequence += str(randint(0, 1))
        for i in range(5):
            fourthStringSequence += str(randint(0, 1))

        text = Text(
            text=f"{firstStringSequence}\n{secondStringSequence}\n{thirdStringSequence}\n{fourthStringSequence}",
            color="#00ff00", font=font
        ).scale(2).to_corner(RIGHT+UP, buff=0.5)

        CCLogo = Text(
            'Coding Club',
            font=font, color="#00ff00"
        ).scale(0.90)\
         .to_corner(LEFT+UP, buff=0.5)\
         .align_to(text, UP)\

        comingUp = Text("Coming Up:", color=GRAY, font=font).scale(0.5)
        presenterName = Text(f"{presenter}", weight=BOLD, color=WHITE, font=font).scale(1.2)

        presenterName.next_to(comingUp, DOWN)
        presenterName.align_to(comingUp, LEFT)

        VGroup(
            presenterName, comingUp
        ).to_corner(LEFT+DOWN, buff=0.5)

        self.add(text, CCLogo, comingUp, presenterName)
        for i in range(5):
            textItem = randint(0, len(text)-1)
            self.play(
                text[textItem].animate.scale(0.5),
                run_time=0.5
            )
            self.play(
                text[textItem].animate.scale(2),
                run_time=0.5
            )

