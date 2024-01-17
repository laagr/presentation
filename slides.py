from manim import *
from manim_slides import Slide

class Titel(Slide):
    def construct(self):
        title = Text("Die Eulersche Zahl", font_size=40)
        subtitle = Text("Richard Laag", font_size=12).next_to(title, DOWN)

        self.play(Write(title), Write(subtitle))

class Intro(Slide):
    def construct(self):
        e_tex = Tex(r"2.7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274274663919320030599218174135966290435729003342952605956307381323286279434907632338298807531952510190115738341879307021540891499348841675092447614606680822648001684774118537423454424371075390777449920695517027618386062613313845830007520449338265602976067371132007093287091274437470472306969772093101416928368190255151086574637721112523897844250569536967707854499699679468644549059879316368892300987931277361782154249992295763514822082698951936680331825288693984964651058209392398294887933203625094431173012381970684161403970198376793206832823764648042953118023287825098194558153017")
        e_tex.next_to(ORIGIN, RIGHT)
        e_tex.generate_target()
        e_tex.target.shift(5 * LEFT - e_tex.get_right())
        self.play(MoveToTarget(e_tex), run_time=5, rate_func=linear)

class Gliederung(Slide):
    def construct(self):
        title = Tex("Gliederung").scale(1.5).to_corner(UP)
        self.play(Write(title), run_time = 1)
        self.wait(1)
        subtitle1 = Text("1.Näherungen", font_size=20)
        subtitle2 = Text("2.Eigenschaften von e", font_size=20).align_to(subtitle1, LEFT).shift(DOWN * 0.5)
        subtitle3 = Text("3.Der Tröpfelalgorithmus\n    3.1.Python", font_size=20).align_to(subtitle2, LEFT).shift(DOWN)
        subtitle4 = Text("4.Zusammenfassung ", font_size=20).align_to(subtitle3, LEFT).shift(DOWN * 1.5)
        self.play(FadeIn(subtitle1), FadeIn(subtitle2), FadeIn(subtitle3), FadeIn(subtitle4))

class Naeherungen(Slide):
    def construct(self):
        title = Tex("Näherungen").scale(1.5).to_corner(UP)
        self.play(Write(title), run_time = 1)
        self.wait(1)

class Eigenschaften(Slide):
    def construct(self):
        title = Tex("Eigenschaften").scale(1.5).to_corner(UP)
        self.play(Write(title), run_time = 1)
        self.wait(1)

class Tropf(Slide):
    def construct(self):
        title = Tex("Der Tröfelalgorithmus").scale(1.5).to_corner(UP)
        self.play(Write(title), run_time = 1)
        self.wait(1)
        table = Tex(r"""
        \def\arraystretch{1.2}
\begin{tabular}{l|l|l|l|l}
  & 2 & 3 & 4 & 5 \\ \hline
2 & 1 & 1 & 1 & 1 \\
  &   &   &   &   \\
  &   &   &   &  
\end{tabular}""")
                       
        
        self.play(FadeIn(table))
        self.next_slide()
        self.play(ReplacementTransform(table[0][17], Tex(r"10").align_to(table[0][17], UL)))
        self.wait()


class Python(Slide):
    def construct(self):
        title = Tex("Python").scale(1.5).to_corner(UP)
        self.play(Write(title), run_time = 1)
        self.wait(1)

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
