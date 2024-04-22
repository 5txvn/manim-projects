from manim import *

class Main(Scene):
    def construct(self):
        #create the intro
        heart1 = ImageMobject("heart.png")
        heart1.shift(LEFT*5)
        heart1.shift(UP*2)
        heart1.rotate(PI/5)
        heart2 = ImageMobject("heart.png")
        heart2.shift(RIGHT*5.7)
        heart2.shift(UP*1.6)
        heart2.rotate(-PI/6)
        heart3 = ImageMobject("heart.png")
        heart3.shift(UP*2.5)
        heart4 = ImageMobject("heart.png")
        heart4.shift(LEFT*4.4)
        heart4.shift(DOWN*2.1)
        heart4.rotate(PI/4)
        heart5 = ImageMobject("heart.png")
        heart5.shift(RIGHT*5.2)
        heart5.shift(DOWN*2.35)
        heart5.rotate(-PI/8)
        heart6 = ImageMobject("heart.png")
        heart6.shift(DOWN*2.5)
        stevenlovesmath = Text("stevenlovesmath!")
        self.play(FadeIn(heart1),FadeIn(heart2),FadeIn(heart3),FadeIn(heart4),FadeIn(heart5),FadeIn(heart6),Write(stevenlovesmath),run_time=2)
        self.wait(3);
        self.play(FadeOut(heart1),FadeOut(heart2),FadeOut(heart3),FadeOut(heart4),FadeOut(heart5),FadeOut(heart6),FadeOut(stevenlovesmath),run_time=1.5)
        self.wait(1);
        #create the main title
        title = Text("Multiplying by 25")
        title.scale(1.5);
        self.play(Write(title),run_time=1.5);
        subtitle = Text("An animation by stevenlovesmath!",color=RED);
        self.wait(0.5);
        self.play(ApplyMethod(title.shift,UP*.5),run_time=1.5);
        subtitle.shift(DOWN*.8);
        self.play(Write(subtitle),run_time=2);
        self.wait(2)
        self.play(FadeOut(title),FadeOut(subtitle),run_time=2);
        self.wait(2)
        #start main scene
        problem = MathTex(r"27\times 25=\dots").scale(2);
        self.play(Write(problem),run_time=2);
        self.play(ApplyMethod(problem.shift,UP*.5),run_time=1);
        explanation1 = MathTex(r"27\div 4=6 \space\mathrm{r}3",color=RED).shift(DOWN*.5);
        self.play(Write(explanation1),run_time=2);
        self.play(Transform(problem,MathTex(r"27\times 25=6\dots").scale(2)),run_time=1);
        self.play(FadeOut(explanation1),run_time=1);
        self.play(ApplyMethod(problem.shift,DOWN*.5),run_time=1);
        start_point = np.array([1, -0.85, 0])
        end_point = np.array([3.5, -0.85, 0])
        arrow = Arrow(start=start_point,end=end_point,color=RED)
        self.play(Create(arrow),run_time=1);
        self.play(FadeOut(arrow),run_time=1);
        self.play(FadeOut(problem))
        table = Table([["Remainder","Ending Digits"],["0","00"],["1","25"],["2","50"],["3","75"]]);
        self.play(Write(table),run_time=2)