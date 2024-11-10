from manim import *
import math


class GoogleLogoAnimation(Scene):
    def construct(self):
        # Create the background
        background_rect = FullScreenRectangle(color=BLACK)
        self.play(FadeIn(background_rect))

        # Create the Google logo elements
        google_text = Text("Google", font_size=108)  # Don't specify color initially
        location_text = Text("Cloud Space | Munich", font_size=36, color=WHITE)

        # Position the location text
        location_text.move_to(DOWN * 1.3)  # Move below the center

        # Add shadows
        google_text.set_shadow(4)

        # Animate the creation of the logo
        self.play(Write(google_text), run_time=2)
        self.play(FadeIn(location_text), run_time=2)  # Animate location text appearance

        # Animate color change to Google colors
        google_colors = [
            "#4285F4",  # Blue
            "#DB4437",  # Red
            "#F4B400",  # Yellow
            "#0F9D58",  # Green
        ]
        color_animations = []
        for i, char in enumerate(google_text.text):
            target_color = google_colors[i % len(google_colors)]  # Cycle through colors
            color_animations.append(FadeToColor(google_text[i], target_color))
        self.play(*color_animations, run_time=1)  # Play all color animations together

        # Let the text stay for 3 seconds
        self.wait(1)  # Pause animation for 3 seconds

        # Unwrite the Google text
        self.play(Unwrite(google_text), run_time=2)
        self.play(Unwrite(location_text), run_time=1)
        self.wait(1)  # Pause animation for 3 seconds

        # Create the additional text with spacing
        offer_text = VGroup(
            Text("We offer", font_size=40),
            Text("1. Executive Briefings", font_size=36, color="#D147BD"),
            Text("|", font_size=10),  # Added spacer text
            Text("--- Technical Labs --- ", font_size=40),  # Added spacer text
            Text("2. Innovation Labs", font_size=36, color=google_colors[0]),
            Text("3. Productivity Labs", font_size=36, color=google_colors[1]),
            Text("4. Solution Labs", font_size=36, color=google_colors[2]),
            Text("5. Build Labs", font_size=36, color=google_colors[3]),
        )
        offer_text.arrange_submobjects(DOWN)

        # Animate flying in the additional text
        self.play(Write(offer_text, run_time=1))

        self.wait(2)  # Short pause before the final message

        # Create the "More info" text
        info_text = Text(
            "More info: https://cloud.google.com/cloud-space",
            font_size=24,
            color=WHITE,
        )
        info_text.move_to(DOWN * 3.5)  # Move to bottom of the screen

        # Animate "More info" text appearing
        self.play(FadeIn(info_text, run_time=1))

        self.wait(5)  # Hold the final message for 5 seconds

# Render the animation
if __name__ == "__main__":
  scene = GoogleLogoAnimation()

  # Configure FFmpeg writer
  writer = ffmpeg_writer = WritingToMovie("google_logo.mp4", fps=30)  # Change filename as desired

  # Render the scene with the writer
  scene.render(writer=writer)
