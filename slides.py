from manim import *
from manim_slides import Slide

class Titel(Slide):
    def construct(self):
        title = Text("Die Eulersche Zahl", font_size=40)
        title.set_color_by_gradient(ORANGE, YELLOW)
        subtitle = Text("Richard Laag", font_size=20).next_to(title, DOWN)
        icon = SVGMobject(f"link.svg").next_to(title, DOWN * 3 + LEFT)
        link = Text("https://laagr.github.io/presentation", font_size = 20).set_color(BLUE).next_to(icon, RIGHT)

        self.play(Write(title), Write(subtitle))
        self.play(DrawBorderThenFill(icon), Write(link))

class Intro(Slide):
    def construct(self):
        e_tex = Tex(r"2.718281828459045235360287471352662497757247093699959574966967627724076630353547594571382178525166427427466391932003059921817413596629043572900334295260595630738132328627943490763233829880753195251019011573834187930702154089149934884167509244761460668082264800168477411853742345442437107539077744992069551702761838606261331384583000752044933826560297606737113200709328709127443747047230696977209310141692836819025515108657463772111252389784425056953696770785449969967946864454905987931636889230098793127736178215424999229576351482208269895193668033182")
        e_tex.next_to(ORIGIN, RIGHT)
        e_tex.generate_target()
        e_tex.target.shift(RIGHT * 8 - e_tex.get_right())

        self.play(MoveToTarget(e_tex), run_time=30, rate_func=rate_functions.ease_in_out_sine)

class Gliederung(Slide):
    def construct(self):

        # Title
        title = Text("Gliederung", font_size=30).to_corner(UL)
        title.set_color_by_gradient(ORANGE, YELLOW)
        self.play(Write(title))

        # 1.
        first_title = Text("1. Eigenschaften von e", font_size=30).next_to(title, DOWN, aligned_edge=LEFT, buff=1)
        first_point1 = Text("- Die Ziffern von E", font_size=20).next_to(first_title, DOWN, aligned_edge=LEFT, buff=0.4)

        # 2.
        second_title = Text("2. Näherungen", font_size=30).next_to(first_point1, DOWN, aligned_edge=LEFT, buff=1)

        # 3.
        third_title = Text("3. Der Tröpfelalgorithmus", font_size=30).next_to(second_title, DOWN,aligned_edge=LEFT, buff=1)
        third_point1 = Text("- Der Algorithmus erklärt", font_size=20).next_to(third_title, DOWN, aligned_edge=LEFT, buff=0.4)
        third_point2 = Text("- Python", font_size=20).next_to(third_point1, DOWN, aligned_edge=LEFT, buff=0.4)

        self.play(Write(first_title), Write(first_point1), Write(second_title), Write(third_title), Write(third_point1), Write(third_point2))


class Eigenschaften:
    def constrict(self):
        # Title
        title = Text("Eigenschaften", font_size=30).to_corner(UL)
        title.set_color_by_gradient(ORANGE, YELLOW)
        self.play(Write(title))

class Naeherungen:
    def constrict(self):
        # Title
        title = Text("Näherungen", font_size=30).to_corner(UL)
        title.set_color_by_gradient(ORANGE, YELLOW)
        self.play(Write(title))

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
        self.play(FadeIn(table))
        self.next_slide()
        
        highlight1 = table.get_cell((2,5), color=RED)
        highlight2 = table.get_cell((1,5), color=RED)
        highitem = table.get_entries((1,9))

        self.play(FadeIn(highlight1), FadeIn(highlight2))
        self.play(Transform(highitem, Text("10").move_to(highitem)))
        self.next_slide()

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
        code = Code(
        code="""
    # Variabeln
    x = 0
    a = [0,2]
    n = smallest_factn_k_digits(precision)
    while n: 
        a.append(1)
        n = n - 1
    i = a.__len__()
    out = ""
    file1 = open("output-tropf.txt", "w")

    # Loop
    while i > 0:
        n = i 
        i = i - 1
        while n > 1:
            n = n - 1
            a[n] = x % n
            x = 10 * a[n - 1] + x // n
        out = out + str(x)

    file1.write(out)
    file1.close()

""",
                    language ="python",
                )

        less_code = Code(
        code ="""
    # Loop
    while i > 0:
        n = i 
        i = i - 1
        while n > 1:
            n = n - 1
            a[n] = x % n
            x = 10 * a[n - 1] + x // n
        out = out + str(x)
""",
                    language ="python",
                )

        self.wipe(title, code)
        self.next_slide()
        self.play(Transform(code, less_code))
        
class Eigenschaften(Slide):
    def construct(self):
        # Title
        title = Text("Eigenschaften", font_size=30).to_corner(UL)
        title.set_color_by_gradient(ORANGE, YELLOW)
        self.play(Write(title))
        
class Naeherungen(Slide):
    def construct(self):
        # Title
        title = Text("Näherungen", font_size=30).to_corner(UL)
        title.set_color_by_gradient(ORANGE, YELLOW)
        self.play(Write(title))

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
