from manim import *
from manim_slides import Slide
import numpy as np

class Titel(Slide):
    def construct(self):
        title = Text("Die Eulersche Zahl", font_size=40).shift(UP)
        title.set_color_by_gradient(ORANGE, YELLOW)
        subtitle = Text("Richard Laag", font_size=20).next_to(title, DOWN)
        icon = SVGMobject(f"link.svg").next_to(title, DOWN * 3).shift(LEFT * 2.5)
        link = Text("https://laagr.github.io/presentation", font_size = 20).set_color(BLUE).next_to(icon, RIGHT)

        self.play(Write(title), Write(subtitle))
        self.play(DrawBorderThenFill(icon), Write(link))

class Intro(Slide):
    def construct(self):
        e_tex = Tex(r"2.718281828459045235360287471352662497757247093699959574966967627724076630353547594571382178525166427427466391932003059921817413596629043572900334295260595630738132328627943490763233829880753195251019011573834187930702154089149934884167509244761460668082264800168477411853742345442437107539077744992069551702761838606261331384583000752044933826560297606737113200709328709127443747047230696977209310141692836819025515108657463772111252389784425056953696770785449969967946864454905987931636889230098793127736178215424999229576351482208269895193668033182")
        e_tex.next_to(ORIGIN, RIGHT)
        e_tex.generate_target()
        e_tex.target.shift(RIGHT * 8 - e_tex.get_right())

        self.play(MoveToTarget(e_tex), run_time=35, rate_func=rate_functions.ease_in_out_sine)

class Gliederung(Slide):
    def construct(self):

        # Title
        title = Text("Gliederung", font_size=30).to_corner(UL)
        title.set_color_by_gradient(ORANGE, YELLOW)
        self.play(Write(title))
        
        euler = ImageMobject(f"Leonhard_Euler.png").scale(0.25)
        euler.to_edge(RIGHT).shift(LEFT)

        quelle = Text("wikimedia.org/wikipedia/commons/d/d7/Leonhard_Euler.jpg",font_size=12).set_color(BLUE)
        quelle.next_to(euler, DOWN)

        # 1.
        first_title = Text("1. Eigenschaften von e", font_size=30).next_to(title, DOWN, aligned_edge=LEFT, buff=0.8)
        first_point1 = Text("- Die Ziffern von e", font_size=20).next_to(first_title, DOWN, aligned_edge=LEFT, buff=0.4)

        # 2.
        second_title = Text("2. Näherungen", font_size=30).next_to(first_point1, DOWN, aligned_edge=LEFT, buff=0.8)
        second_point1 = Text("- e als Limes, Summe und Kettenbruch", font_size=20).next_to(second_title, DOWN, aligned_edge=LEFT, buff=0.4)

        # 3.
        third_title = Text("3. Der Tröpfelalgorithmus", font_size=30).next_to(second_point1, DOWN,aligned_edge=LEFT, buff=0.8)
        third_point1 = Text("- Erklärung des Algorithmus", font_size=20).next_to(third_title, DOWN, aligned_edge=LEFT, buff=0.4)
        third_point2 = Text("- Python", font_size=20).next_to(third_point1, DOWN, aligned_edge=LEFT, buff=0.4)

        self.play(Write(first_title), Write(first_point1), Write(second_title), Write(second_point1), Write(third_title), Write(third_point1), Write(third_point2), Write(quelle), FadeIn(euler))
        self.wait()

class Naeherungen(Slide):
    def construct(self):
        # Title
        title = Text("Näherungen", font_size=30).to_corner(UL)
        title.set_color_by_gradient(ORANGE, YELLOW)
        self.play(Write(title))

        lim = MathTex("e", "= \\lim_{n \\to \\infty}", "\\left(1 + \\frac{1}{n}\\right)^n")
        lim_ex = VGroup(
                MathTex("\\left(1 + \\frac{1}{10}\\right)^{10}"),
                MathTex("\\left(1 + \\frac{1}{100}\\right)^{100}"),
                MathTex("\\left(1 + \\frac{1}{1000}\\right)^{1000}"))

        lim_ex_sol = VGroup(
                MathTex("\\left(1 + \\frac{1}{10}\\right)^{10}", "= 2.59\\dots"),
                MathTex("\\left(1 + \\frac{1}{100}\\right)^{100}", "= 2,704\\dots"),
                MathTex("\\left(1 + \\frac{1}{1000}\\right)^{1000}", "= 2,7169\\dots"))

        lim_ex.arrange(DOWN, aligned_edge=LEFT)
        lim_ex_sol.arrange(DOWN, aligned_edge=LEFT)

        self.play(Write(lim))
        self.next_slide()
        self.play(Transform(lim, lim_ex))
        self.next_slide()
        self.play(Transform(lim, lim_ex_sol))
        self.next_slide()
        self.play(FadeOut(lim))

        taylor_series = MathTex(
            "e^x", "=", "1", "+", "x", "+", "\\frac{x^2}{2!}", "+", "\\frac{x^3}{3!}", "+", "\\cdots"
        )

        e_nae = MathTex(
            "e", "=", "1", "+", "1", "+", "\\frac{1}{1 \\times 2}", "+", "\\frac{1}{1 \\times 2 \\times 3}", "+", "\\cdots"
        )

        e = MathTex("e", "=", "2.71", "\\cdots")

        self.play(Write(taylor_series))
        self.next_slide()
        self.play(Transform(taylor_series, e_nae))
        self.next_slide()
        self.play(Transform(taylor_series, e))
        self.next_slide()
        self.play(FadeOut(taylor_series))

        kettenbruch = MathTex("e", "=", "2", "+\\frac{1}{1 + \\frac{1}{2 + \\frac{1}{1 + \\frac{1}{1 + \\frac{1}{4 + \\frac{1}{\\dots}}}}}}"
)
        self.play(Write(kettenbruch))
        self.next_slide()
        self.play(Transform(kettenbruch, e))

        self.wait()

class Tropf(Slide):
    def construct(self):
        # Title
        title = Text("Der Tröpfelalgorithmus", font_size=30).to_corner(UL)
        title.set_color_by_gradient(ORANGE, YELLOW)
        self.play(Write(title))

        table = Table([[" ","2","3","4","5"],["2","1","1","1","1"],["7","0","1","0","0"],["1","1","1","0","0"]], include_outer_lines=True).next_to(title, DOWN, aligned_edge=LEFT)
        entries = table.get_entries()
        n = 0
        for item in entries:
            if n > 8:
                item.set_color(BLACK)  
            n = n + 1
        self.play(Create(table))
        self.wait()
        self.next_slide()

        highlight1 = table.get_cell((2,5), color=RED)
        highlight2 = table.get_cell((1,5), color=RED)
        highitem = table.get_entries((1,9))

        self.play(FadeIn(highlight1), FadeIn(highlight2))
        self.play(Transform(highitem, Text("10").move_to(highitem)))

        clone1 = Text("%  5  =  ")
        clone2 = Text("//  5  =  ")
        ans1 = Text("0").set_color(BLACK)
        ans2 = Text("2").set_color(BLACK)
        a = highitem.copy()

        equation1 = VGroup(highitem.copy(), clone1, ans1)
        equation2 = VGroup(a, clone2, ans2)

        equation1.arrange(RIGHT, buff=0.4)
        equation1.next_to(table, RIGHT, buff=1)
        equation2.arrange(RIGHT, buff=0.4)
        equation2.next_to(equation1, DOWN, aligned_edge=LEFT, buff=1)

        self.play(Write(equation1), Write(equation2))
        self.play(FadeIn(ans1.set_color(YELLOW)), FadeIn(ans2.set_color(BLUE)))

        self.next_slide()

        self.play(Transform(ans1, table.get_entries((1,14)).copy().set_color(WHITE)))
        table.get_entries((1,14)).set_color(WHITE)
        o = table.get_entries((1,8))

        self.next_slide()

        self.play(Transform(o, Text("10").move_to(o)))
        self.wait()
        self.play(Transform(ans2, Text("12").move_to(o)), FadeOut(o))

        self.next_slide()

        self.play(FadeOut(highlight1),FadeOut(highlight2),FadeOut(equation1),FadeOut(clone2), FadeOut(a), Transform(ans2, Text("1").move_to(o)), Transform(table.get_entries((1,9)), Text("1").move_to(table.get_entries((1,9)))))
        self.play(Write(table.get_rows()[2].copy().set_color(WHITE), reverse=True, remover=False))
        table.get_rows()[3].set_color(WHITE)
        self.play(Write(table.get_rows()[3], reverse=True, remover=False))

class Python(Slide):
    def construct(self):
        # Title
        title = Text("Python", font_size=30).to_corner(UL)
        title.set_color_by_gradient(ORANGE, YELLOW)
        self.play(Write(title))

        variabeln = VGroup(
                Tex("a = [0, 2, 1, 1, 1, \\dots]", font_size=30), 
                Text("precision = Anzahl an Nachkommastellen", font_size=20),
                Tex("x = 10", font_size=30), 
                )

        variabeln.arrange(DOWN,aligned_edge=LEFT)

        code = Code(
                code ="""while precision > 0:
        n = a.__len__() 
        precision = precision - 1

        while n > 1:
            n = n - 1
            a[n] = x % n
            x = 10 * a[n - 1] + x // variabeln

        out = out + str(x)""",
        language ="python",
        )

        code.shift(DOWN * 1.5)
        variabeln.next_to(code, UP)

        self.play(Create(code), Write(variabeln))
        self.wait()
        self.next_slide()
        self.play(FadeOut(title), FadeOut(code), FadeOut(variabeln))

class Eigenschaften(Slide):
    def construct(self):
        # Title
        title = Text("Eigenschaften", font_size=30).to_corner(UL)
        title.set_color_by_gradient(ORANGE, YELLOW)
        self.play(Write(title))
        liste = VGroup(
                Text("- e ist irrational", font_size=20),
                Text("- e ist eine normale Zahl", font_size=20),
                Text("-> alle Ziffern sind gleichmäßig verteilt", font_size=20),
                Text("- absolut normal", font_size=20),
                Text("-> normal in allen Basen", font_size=20),
                Text("- Die Funktion eˣ ist eigene Ableitung", font_size=20)
                )

        liste.arrange(DOWN, aligned_edge=LEFT).to_edge(LEFT)
        barchart = self.create_bar_chart()

        axis = Axes(
                x_range=[0,1,1],
                y_range=[0,125,25],
                axis_config={"include_numbers": True},
                x_length=10,
                y_length=5,
        )

        axis.next_to(barchart, LEFT, aligned_edge=LEFT, buff = 0.17).shift(UP * 0.15).shift(RIGHT * 4.6)

        self.play(Write(liste), Create(barchart), Create(axis))
        self.next_slide()
        self.play(FadeOut(liste), FadeOut(barchart), FadeOut(axis))

        axes_left = Axes(
            x_range=[0, 3, 1],
            y_range=[0, 20, 4],
            axis_config={"color": BLUE, "include_numbers": True},
            x_length=5
        )
        axes_left.next_to(title, DOWN * 1.4, aligned_edge=LEFT)
        axes_right = Axes(
            x_range=[0, 3, 1],
            y_range=[0, 20, 4],
            axis_config={"color": RED, "include_numbers": True},
            x_length=5
        )
        axes_right.next_to(axes_left, RIGHT)
        axes_right.to_edge(RIGHT)

        labels_right = axes_right.get_axis_labels(
            Tex("t in s").scale(0.8), Text("v in m/s").scale(0.5))

        labels_left = axes_left.get_axis_labels(
            Tex("t in s").scale(0.8), Text("s in m").scale(0.5))


        graph_left = axes_left.plot(lambda x: np.exp(x), color=WHITE)
        graph_right = axes_right.plot(lambda x: np.exp(x), color=WHITE)

        self.wait()
        self.play(Create(axes_left), Create(axes_right))
        self.play(Create(graph_left), Create(graph_right))
        self.play(Write(labels_right), Write(labels_left))

    def create_bar_chart(self):
        data= [4.04,3.84,3.88,4.36,4,3.4,3.96,3.96,4.12,4.48]
        bars = VGroup()

        for i, val in enumerate(data):
            bar = Rectangle(height=val, width=0.4, fill_opacity=0.8, fill_color=BLUE)
            bar.next_to(ORIGIN, RIGHT * 1.2,aligned_edge=DOWN, buff = 0.3)
            bar.shift(RIGHT * i * 0.7).shift(DOWN * 2.4)
            bars.add(bar)
            bars.add(Text(str(i), font_size=20).next_to(bar, DOWN * 0.75))

        bars.add(Text("1000 Ziffern von e", font_size=20).to_corner(UR).shift(DOWN).shift(LEFT * 2))
        return bars

