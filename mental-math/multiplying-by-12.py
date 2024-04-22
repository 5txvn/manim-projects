from manim import *

class Main(Scene):
    def construct(self):
        #add the video sound
        self.add_sound("multiplying-by-12.wav")
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
        self.wait(6.5);
        #create main title
        title = Text("Multiplying by 12")
        title.scale(1.5);
        self.play(Write(title),run_time=2);
        subtitle = Text("An animation by stevenlovesmath!",color=RED);
        self.wait(0.5);
        self.play(ApplyMethod(title.shift,UP*.5),run_time=2);
        subtitle.shift(DOWN*.8);
        self.play(Write(subtitle),run_time=2);
        self.wait(2)
        self.play(FadeOut(title),FadeOut(subtitle),run_time=2);
        #22
        self.wait(6)
        #create first problem
        problem = MathTex(r"31\times 12=\dots").scale(2);
        self.play(Write(problem),run_time=2);
        self.wait(8);
        #39
        #self.play(Transform(problem,VGroup(MathTex(r"3"),MathTex(r"1",color=RED),MathTex(r"\times 12=\dots")).arrange(RIGHT,buff=0.05).shift(UP*.5).scale(2)),run_time=0.1)
        self.play(ApplyMethod(problem.shift,UP*0.5),run_time=1);
        explanation1 = MathTex(r"1\times 2=2",color=RED).shift(DOWN*.5)
        self.play(Write(explanation1),run_time=2);
        self.wait(2)
        #44
        self.play(Transform(problem,MathTex(r"31\times 12=\dots 2").scale(2).shift(UP*.5)),run_time=1)
        self.play(FadeOut(explanation1),run_time=1);
        self.play(ApplyMethod(problem.shift,DOWN*.5),run_time=1);
        self.wait(2.5)
        start_point = np.array([3.5, -0.85, 0])
        end_point = np.array([1, -0.85, 0])
        arrow = Arrow(start=start_point,end=end_point,color=RED)
        self.play(Create(arrow),run_time=1.5);
        self.wait(2)
        self.play(FadeOut(arrow),run_time=1);
        #54
        #next animation
        self.play(ApplyMethod(problem.shift,UP*.5),run_time=1);
        explanation2 = MathTex(r"3\times 2+1=7",color=RED).shift(DOWN*.5);
        self.play(Write(explanation2),run_time=2);
        #57
        self.wait(7)
        self.play(Transform(problem,MathTex(r"31\times 12=\dots 72").scale(2).shift(UP*.5)),run_time=1);
        self.wait(1)
        self.play(FadeOut(explanation2),run_time=1);
        self.play(ApplyMethod(problem.shift,DOWN*.5),run_time=1);
        #68
        #final animation
        self.wait(4)
        self.play(Transform(problem,MathTex(r"31\times 12=372").scale(2)),run_time=1);
        self.wait(2)
        self.play(FadeOut(problem),run_time=1);
        #76
        #second problem
        self.wait(2.5)
        problem = MathTex(r"68\times 12=\dots").scale(2);
        self.play(Write(problem),run_time=2);
        #80.5
        self.wait(0.5)
        self.play(ApplyMethod(problem.shift,UP*.5),run_time=1);
        explanation1 = MathTex(r"8\times 2=16",color=RED).shift(DOWN*.5);
        self.play(Write(explanation1),run_time=2);
        #84
        self.wait(9)
        self.play(Transform(problem,MathTex(r"68\times 12=\dots 6").scale(2).shift(UP*.5)),run_time=1);
        self.play(FadeOut(explanation1),run_time=1);
        self.play(ApplyMethod(problem.shift,DOWN*.5),run_time=1);
        #next animation
        self.wait(3)
        self.play(ApplyMethod(problem.shift,UP*.5),run_time=1);
        explanation2 = MathTex(r"(6\times 2+8)+1=21",color=RED).shift(DOWN*.5);
        self.play(Write(explanation2),run_time=2);
        #102
        self.wait(6)
        self.play(Transform(problem,MathTex(r"68\times 12=\dots 16").scale(2).shift(UP*.5)),run_time=1);
        self.play(FadeOut(explanation2),run_time=1);
        self.play(ApplyMethod(problem.shift,DOWN*.5),run_time=1);
        #111
        #final explanation
        self.wait(4)
        self.play(ApplyMethod(problem.shift,UP*.5),run_time=1);
        explanation2 = MathTex(r"6+2=8",color=RED).shift(DOWN*.5);
        self.play(Write(explanation2),run_time=2);
        #118
        self.play(Transform(problem,MathTex(r"68\times 12=816").scale(2).shift(UP*.5)),run_time=1);
        self.play(FadeOut(explanation2),run_time=1);
        self.play(ApplyMethod(problem.shift,DOWN*.5),run_time=1);
        self.wait(2)
        self.play(FadeOut(problem),run_time=1);
        self.wait(3)

        #last problem
        #7
        problem = MathTex(r"537\times 12=\dots").scale(2);
        self.play(Write(problem),run_time=2);
        self.wait(1)
        self.play(ApplyMethod(problem.shift,UP*.5),run_time=1);
        explanation1 = MathTex(r"7\times 2=14",color=RED).shift(DOWN*.5);
        self.play(Write(explanation1),run_time=2);
        #13
        self.wait(1)
        self.play(Transform(problem,MathTex(r"537\times 12=\dots 4").scale(2).shift(UP*.5)),run_time=1);
        self.play(FadeOut(explanation1),run_time=1);
        self.play(ApplyMethod(problem.shift,DOWN*.5),run_time=1);
        #17
        #next animation
        self.wait(1)
        self.play(ApplyMethod(problem.shift,UP*.5),run_time=1);
        explanation2 = MathTex(r"(3\times 2+7)+1=14",color=RED).shift(DOWN*.5);
        self.play(Write(explanation2),run_time=2);
        #20
        self.wait(8.5)
        self.play(Transform(problem,MathTex(r"537\times 12=\dots 44").scale(2).shift(UP*.5)),run_time=1);
        self.play(FadeOut(explanation2),run_time=1);
        #self.play(ApplyMethod(problem.shift,DOWN*.5),run_time=1);
        self.wait(1.5)
        #32
        #next animation
        #self.play(ApplyMethod(problem.shift,UP*.5),run_time=1);
        explanation2 = MathTex(r"(5\times 2+3)+1=14",color=RED).shift(DOWN*.5);
        self.play(Write(explanation2),run_time=2);
        self.wait(6)
        self.play(Transform(problem,MathTex(r"537\times 12=\dots 444").scale(2).shift(UP*.5)),run_time=1);
        self.play(FadeOut(explanation2),run_time=1);
        #self.play(ApplyMethod(problem.shift,DOWN*.5),run_time=1);
        self.wait(1)
        #44
        #final explanation
        #self.play(ApplyMethod(problem.shift,UP*.5),run_time=1);
        explanation2 = MathTex(r"5+1=6",color=RED).shift(DOWN*.5);
        self.play(Write(explanation2),run_time=2);
        self.wait(.5)
        self.play(Transform(problem,MathTex(r"357\times 12=6444").scale(2).shift(UP*.5)),run_time=1);
        self.play(FadeOut(explanation2),run_time=1);
        self.play(ApplyMethod(problem.shift,DOWN*.5),run_time=1);
        self.play(FadeOut(problem),run_time=1);