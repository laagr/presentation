from manim import *
from manim_slides import Slide

class Titel(Slide):
    def construct(self):
        title = Text("Die Eulersche Zahl", font_size=40)
        subtitle = Text("Richard Laag", font_size=12).next_to(title, DOWN)

        self.play(Write(title), Write(subtitle))

class Intro(Slide):
    def construct(self):
        e_tex = Tex(r"2.718281828459045235360287471352662497757247093699959574966967627724076630353547594571382178525166427427466391932003059921817413596629043572900334295260595630738132328627943490763233829880753195251019011573834187930702154089149934884167509244761460668082264800168477411853742345442437107539077744992069551702761838606261331384583000752044933826560297606737113200709328709127443747047230696977209310141692836819025515108657463772111252389784425056953696770785449969967946864454905987931636889230098793127736178215424999229576351482208269895193668033182")
        e_tex.next_to(ORIGIN, RIGHT)
        e_tex.generate_target()
        e_tex.target.shift(RIGHT * 8 - e_tex.get_right())

        self.play(MoveToTarget(e_tex), run_time=30, rate_func=rate_functions.ease_out_sine)

        self.next_slide()

        e_tex.generate_target()
        e_tex.target.shift(UP * 8)

        self.play(MoveToTarget(e_tex), run_time=1.5)

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
