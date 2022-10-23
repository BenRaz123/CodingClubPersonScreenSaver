from manim import *
from random import randint

presenter = "John Bananas"
font = "Space Mono"


class CodingClubPersonScreenSaver(Scene):
    def construct(self):
        (
            firstStringSequence,
            secondStringSequence,
            thirdStringSequence,
            fourthStringSequence,
            fifthStringSequence,
            sixthStringSequence,
            seventhStringSequence,
        ) = ("", "", "", "", "", "", "")

        for i in range(18):
            firstStringSequence += str(randint(0, 1))
        for i in range(18):
            secondStringSequence += str(randint(0, 1))
        for i in range(18):
            thirdStringSequence += str(randint(0, 1))
        for i in range(18):
            fourthStringSequence += str(randint(0, 1))
        for i in range(18):
            fifthStringSequence += str(randint(0, 1))
        for i in range(18):
            sixthStringSequence += str(randint(0, 1))
        for i in range(18):
            seventhStringSequence += str(randint(0, 1))

        text = (
            Text(
                text=f"{firstStringSequence}\n{secondStringSequence}\n{thirdStringSequence}\n{fourthStringSequence}\n{fifthStringSequence}\n{sixthStringSequence}\n{seventhStringSequence}",
                color="#222",
                font=font,
            )
            .scale(2)
            .center()
        )

        CCLogo = (
            Text("Coding Club", font=font, color="#00ff00")
            .scale(0.90)
            .to_corner(LEFT + UP, buff=0.5)
        )

        comingUp = Text("Coming Up:", color=GRAY, font=font).scale(0.5)
        presenterName = Text(
            f"{presenter}", weight=BOLD, color="#0f0", font=font
        ).scale(1.2)

        presenterName.next_to(comingUp, DOWN)
        presenterName.align_to(comingUp, LEFT)

        VGroup(presenterName, comingUp).to_corner(LEFT + DOWN, buff=0.5)

        self.add(text)
        self.add(CCLogo, comingUp, presenterName)
        VGroup(CCLogo, comingUp, presenterName).set_z_index(0)

        for i in range(20):
            textItem = randint(0, len(text) - 1)
            self.play(text[textItem].animate.scale(0.5), run_time=0.5)
            self.play(text[textItem].animate.scale(2), run_time=0.5)
