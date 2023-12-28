from manim import *
from manim_slides import Slide

class Titel(Scene):
    def construct(self):
        title = Text("die Eulersche Zahl", font_size=40)
        subtitle = Text("Richard Laag", font_size=12).next_to(title, DOWN)

        self.play(Write(title), Write(subtitle))

class Intro(Slide):
    def construct(self):
        e_tex = Tex(r"2.7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274274663919320030599218174135966290435729003342952605956307381323286279434907632338298807531952510190115738341879307021540891499348841675092447614606680822648001684774118537423454424371075390777449920695517027618386062613313845830007520449338265602976067371132007093287091274437470472306969772093101416928368190255151086574637721112523897844250569536967707854499699679468644549059879316368892300987931277361782154249992295763514822082698951936680331825288693984964651058209392398294887933203625094431173012381970684161403970198376793206832823764648042953118023287825098194558153017")
        e_tex.next_to(ORIGIN, RIGHT)
        e_tex.generate_target()
        e_tex.target.shift(5 * LEFT - e_tex.get_right())
        self.play(MoveToTarget(e_tex), run_time=150, rate_func=linear)        
        self.play(FadeOut(e_tex))

class Gliederung(Slide):
    def construct(self):
        title = Text("Gliederung", font_size=28).move_to(UL)
        subtitle1 = Text("Gliederung", font_size=16)
        self.play(Write(title), Write(subtitle1))      


class WithTeX(Slide):
    def construct(self):
        tex, text = VGroup(
            Tex(r"You can also use \TeX, e.g., $\cos\theta=1$"),
            Text("which does not render like plain text"),
        ).arrange(DOWN)

        self.play(FadeIn(tex))
        self.next_slide()

        self.play(FadeIn(text, shift=DOWN))


class Outro(Slide):
    def construct(self):
        learn_more = VGroup(
            Text("Learn more about Manim Slides:"),
            Text("https://manim-slides.eertmans.be"),
        ).arrange(DOWN)

        self.play(FadeIn(learn_more))
