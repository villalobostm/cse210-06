from constants import *
from game.casting.animation import Animation
from game.casting.ball import Ball
from game.casting.body import Body
from game.casting.image import Image
from game.casting.label import Label
from game.casting.point import Point
from game.casting.racket import Racket
from game.casting.stats import Stats
from game.casting.text import Text 
from game.scripting.change_scene_action import ChangeSceneAction
from game.scripting.collide_borders_action import CollideBordersAction
from game.scripting.collide_racket_action import CollideRacketAction
from game.scripting.control_racket_action import ControlRacketAction
from game.scripting.draw_ball_action import DrawBallAction
from game.scripting.draw_dialog_action import DrawDialogAction
from game.scripting.draw_hud_action import DrawHudAction
from game.scripting.draw_racket_action import DrawRacketAction
from game.scripting.end_drawing_action import EndDrawingAction
from game.scripting.initialize_devices_action import InitializeDevicesAction
from game.scripting.load_assets_action import LoadAssetsAction
from game.scripting.move_ball_action import MoveBallAction
from game.scripting.move_racket_action import MoveRacketAction
from game.scripting.play_sound_action import PlaySoundAction
from game.scripting.release_devices_action import ReleaseDevicesAction
from game.scripting.start_drawing_action import StartDrawingAction
from game.scripting.timed_change_scene_action import TimedChangeSceneAction
from game.scripting.unload_assets_action import UnloadAssetsAction
from game.services.raylib.raylib_audio_service import RaylibAudioService
from game.services.raylib.raylib_keyboard_service import RaylibKeyboardService
from game.services.raylib.raylib_physics_service import RaylibPhysicsService
from game.services.raylib.raylib_video_service import RaylibVideoService
from game.scripting.draw_button_action import DrawButtonAction
from game.casting.button import Button
from game.services.raylib.raylib_mouse_service import RaylibMouseService
from game.scripting.change_scene_click_action import ChangeSceneClickAction

class SceneManager:
    """The person in charge of setting up the cast and script for each scene."""
    
    AUDIO_SERVICE = RaylibAudioService()
    KEYBOARD_SERVICE = RaylibKeyboardService()
    PHYSICS_SERVICE = RaylibPhysicsService()
    VIDEO_SERVICE = RaylibVideoService(GAME_NAME, SCREEN_WIDTH, SCREEN_HEIGHT)
    MOUSE_SERVICE = RaylibMouseService()

    COLLIDE_BORDERS_ACTION = CollideBordersAction(PHYSICS_SERVICE, AUDIO_SERVICE, STATS_GROUP_P1, STATS_GROUP_P2)
    P1_COLLIDE_RACKET_ACTION = CollideRacketAction(PHYSICS_SERVICE, AUDIO_SERVICE,RACKET_GROUP_P1)
    P2_COLLIDE_RACKET_ACTION = CollideRacketAction(PHYSICS_SERVICE, AUDIO_SERVICE,RACKET_GROUP_P2)
    P1_CONTROL_RACKET_ACTION = ControlRacketAction(KEYBOARD_SERVICE,RACKET_GROUP_P1,P1_UP,P1_DOWN)
    P2_CONTROL_RACKET_ACTION = ControlRacketAction(KEYBOARD_SERVICE,RACKET_GROUP_P2,P2_UP,P2_DOWN)
    DRAW_BALL_ACTION = DrawBallAction(VIDEO_SERVICE)
    DRAW_DIALOG_ACTION = DrawDialogAction(VIDEO_SERVICE)
    P1_DRAW_HUD_ACTION = DrawHudAction(VIDEO_SERVICE, STATS_GROUP_P1, SCORE_GROUP_P1)
    P2_DRAW_HUD_ACTION = DrawHudAction(VIDEO_SERVICE, STATS_GROUP_P2, SCORE_GROUP_P2)
    P1_DRAW_RACKET_ACTION= DrawRacketAction(VIDEO_SERVICE,RACKET_GROUP_P1)
    P2_DRAW_RACKET_ACTION= DrawRacketAction(VIDEO_SERVICE,RACKET_GROUP_P2)
    END_DRAWING_ACTION = EndDrawingAction(VIDEO_SERVICE)
    INITIALIZE_DEVICES_ACTION = InitializeDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    LOAD_ASSETS_ACTION = LoadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)
    MOVE_BALL_ACTION = MoveBallAction()
    P1_MOVE_RACKET_ACTION = MoveRacketAction(RACKET_GROUP_P1)
    P2_MOVE_RACKET_ACTION = MoveRacketAction(RACKET_GROUP_P2)
    RELEASE_DEVICES_ACTION = ReleaseDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    START_DRAWING_ACTION = StartDrawingAction(VIDEO_SERVICE)
    UNLOAD_ASSETS_ACTION = UnloadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)

    DRAW_BUTTON_1_ACTION = DrawButtonAction(VIDEO_SERVICE, BUTTON_1_GROUP)
    DRAW_BUTTON_2_ACTION = DrawButtonAction(VIDEO_SERVICE, BUTTON_2_GROUP)
    DRAW_BUTTON_3_ACTION = DrawButtonAction(VIDEO_SERVICE, BUTTON_3_GROUP)

    def __init__(self):
        pass

    def prepare_scene(self, scene, cast, script):
        if scene == MENU:
            self._prepare_menu(cast, script)
        elif scene == NEW_GAME:
            self._prepare_new_game(cast, script)
        elif scene == NEXT_LEVEL:
            self._prepare_next_level(cast, script)
        elif scene == TRY_AGAIN:
            self._prepare_try_again(cast, script)
        elif scene == IN_PLAY:
            self._prepare_in_play(cast, script)
        elif scene == GAME_OVER:    
            self._prepare_game_over(cast, script)
    
    # ----------------------------------------------------------------------------------------------
    # scene methods
    # ----------------------------------------------------------------------------------------------
    def _prepare_menu(self, cast, script):
        self._add_button(cast, BUTTON_1_GROUP, BUTTON_1_Y_POSITION, BUTTON_1_X_POSITION, BUTTON_1_WIDTH, BUTTON_1_HEIGHT, BUTTON_1_IMAGE, BUTTON_1_TEXT)
        self._add_button(cast, BUTTON_2_GROUP, BUTTON_2_Y_POSITION, BUTTON_2_X_POSITION, BUTTON_2_WIDTH, BUTTON_2_HEIGHT, BUTTON_2_IMAGE, BUTTON_2_TEXT)
        self._add_button(cast, BUTTON_3_GROUP, BUTTON_3_Y_POSITION, BUTTON_3_X_POSITION, BUTTON_3_WIDTH, BUTTON_3_HEIGHT, BUTTON_3_IMAGE, BUTTON_3_TEXT)

        self._add_initialize_script(script)
        self._add_load_script(script)
        script.clear_actions(INPUT)
        script.add_action(INPUT, ChangeSceneAction(self.KEYBOARD_SERVICE, NEW_GAME))
        # script.add_action(INPUT, ChangeSceneClickAction(self.MOUSE_SERVICE, BUTTON_1_X_POSITION, BUTTON_1_Y_POSITION, NEW_GAME))
        self._add_menu_output_script(script)
        self._add_unload_script(script)
        self._add_release_script(script)

       

    def _prepare_new_game(self, cast, script):
        self._add_stats(cast, STATS_GROUP_P1)
        self._add_stats(cast, STATS_GROUP_P2)
        self._add_score(cast, SCORE_GROUP_P1, SCORE_P1_X_POSITION)
        self._add_score(cast, SCORE_GROUP_P2, SCORE_P2_X_POSITION)
        self._add_ball(cast)

        self._add_racket(cast,RACKET_GROUP_P1,RACKET_POSITION_P1)
        self._add_racket(cast,RACKET_GROUP_P2,RACKET_POSITION_P2)
        self._add_dialog(cast, ENTER_TO_START)

        self._add_initialize_script(script)
        self._add_load_script(script)
        script.clear_actions(INPUT)
        script.add_action(INPUT, ChangeSceneAction(self.KEYBOARD_SERVICE, NEXT_LEVEL))
        self._add_output_script(script)
        self._add_unload_script(script)
        self._add_release_script(script)
        
    def _prepare_next_level(self, cast, script):
        self._add_ball(cast)
        self._add_racket(cast,RACKET_GROUP_P1,RACKET_POSITION_P1)
        self._add_racket(cast,RACKET_GROUP_P2,RACKET_POSITION_P2)
        self._add_dialog(cast, PREP_TO_LAUNCH)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_output_script(script)
        script.add_action(OUTPUT, PlaySoundAction(self.AUDIO_SERVICE, WELCOME_SOUND))
        
    def _prepare_try_again(self, cast, script):
        self._add_ball(cast)
        self._add_racket(cast,RACKET_GROUP_P1,RACKET_POSITION_P1)
        self._add_racket(cast,RACKET_GROUP_P2,RACKET_POSITION_P2)
        self._add_dialog(cast, PREP_TO_LAUNCH)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_in_play(self, cast, script):
        self._activate_ball(cast)
        cast.clear_actors(DIALOG_GROUP)

        script.clear_actions(INPUT)
        script.add_action(INPUT, self.P1_CONTROL_RACKET_ACTION)
        script.add_action(INPUT, self.P2_CONTROL_RACKET_ACTION)
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_game_over(self, cast, script):
        self._add_ball(cast)
        self._add_racket(cast,RACKET_GROUP_P1,RACKET_POSITION_P1)
        self._add_racket(cast,RACKET_GROUP_P2,RACKET_POSITION_P2)
        self._add_dialog(cast, WAS_GOOD_GAME)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(NEW_GAME, 5))
        script.clear_actions(UPDATE)
        self._add_output_script(script)

    # ----------------------------------------------------------------------------------------------
    # casting methods
    # ----------------------------------------------------------------------------------------------
    
    def _activate_ball(self, cast):
        ball = cast.get_first_actor(BALL_GROUP)
        ball.release()

    def _add_ball(self, cast):
        cast.clear_actors(BALL_GROUP)
        x = CENTER_X - BALL_WIDTH / 2
        y = CENTER_Y - BALL_HEIGHT / 2
        position = Point(x, y)
        size = Point(BALL_WIDTH, BALL_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Image(BALL_IMAGE)
        ball = Ball(body, image, True)
        cast.add_actor(BALL_GROUP, ball)

    def _add_dialog(self, cast, message):
        cast.clear_actors(DIALOG_GROUP)
        text = Text(message, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, CENTER_Y)
        label = Label(text, position)
        cast.add_actor(DIALOG_GROUP, label)

    def _add_level(self, cast):
        cast.clear_actors(LEVEL_GROUP)
        text = Text(LEVEL_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_LEFT)
        position = Point(HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(LEVEL_GROUP, label)

    def _add_lives(self, cast):
        cast.clear_actors(LIVES_GROUP)
        text = Text(LIVES_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_RIGHT)
        position = Point(SCREEN_WIDTH - HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(LIVES_GROUP, label)

    def _add_score(self, cast, player, x_position):
        cast.clear_actors(player)
        text = Text(SCORE_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(x_position, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(player, label)

    def _add_stats(self, cast, player_stats):
        cast.clear_actors(player_stats)
        stats = Stats()
        cast.add_actor(player_stats, stats)

    def _add_racket(self, cast, player, x_position):
        cast.clear_actors(player)
        x = x_position
        y = CENTER_Y - (RACKET_HEIGHT / 2)
        position = Point(x, y)
        size = Point(RACKET_WIDTH, RACKET_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        animation = Animation(RACKET_IMAGES, RACKET_RATE)
        racket = Racket(body, animation)
        cast.add_actor(player, racket)

    def _add_button(self, cast, button_group, y_position, x_position, width, height, image, text_button):
        cast.clear_actors(button_group)
        x = x_position
        y = y_position
        position = Point(x, y)
        size = Point(width, height)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Image(image)
        button = Button(body, image, True)
        cast.add_actor(button_group, button)

    # ----------------------------------------------------------------------------------------------
    # scripting methods
    # ----------------------------------------------------------------------------------------------
    def _add_initialize_script(self, script):
        script.clear_actions(INITIALIZE)
        script.add_action(INITIALIZE, self.INITIALIZE_DEVICES_ACTION)

    def _add_load_script(self, script):
        script.clear_actions(LOAD)
        script.add_action(LOAD, self.LOAD_ASSETS_ACTION)
    
    def _add_output_script(self, script):
        script.clear_actions(OUTPUT)
        script.add_action(OUTPUT, self.START_DRAWING_ACTION)
        script.add_action(OUTPUT, self.P1_DRAW_HUD_ACTION)
        script.add_action(OUTPUT, self.P2_DRAW_HUD_ACTION)
        script.add_action(OUTPUT, self.DRAW_BALL_ACTION)
        script.add_action(OUTPUT, self.P1_DRAW_RACKET_ACTION)
        script.add_action(OUTPUT, self.P2_DRAW_RACKET_ACTION)
        script.add_action(OUTPUT, self.DRAW_DIALOG_ACTION)
        script.add_action(OUTPUT, self.END_DRAWING_ACTION)

    def _add_release_script(self, script):
        script.clear_actions(RELEASE)
        script.add_action(RELEASE, self.RELEASE_DEVICES_ACTION)
    
    def _add_unload_script(self, script):
        script.clear_actions(UNLOAD)
        script.add_action(UNLOAD, self.UNLOAD_ASSETS_ACTION)
        
    def _add_update_script(self, script):
        script.clear_actions(UPDATE)
        script.add_action(UPDATE, self.MOVE_BALL_ACTION)
        script.add_action(UPDATE, self.P1_MOVE_RACKET_ACTION)
        script.add_action(UPDATE, self.P2_MOVE_RACKET_ACTION)
        script.add_action(UPDATE, self.COLLIDE_BORDERS_ACTION)
        script.add_action(UPDATE, self.P1_COLLIDE_RACKET_ACTION)
        script.add_action(UPDATE, self.P2_COLLIDE_RACKET_ACTION)
        script.add_action(UPDATE, self.P1_MOVE_RACKET_ACTION)
        script.add_action(UPDATE, self.P2_MOVE_RACKET_ACTION)

    def _add_menu_output_script(self, script):
        script.clear_actions(OUTPUT)
        script.add_action(OUTPUT, self.START_DRAWING_ACTION)
        script.add_action(OUTPUT, self.DRAW_BUTTON_1_ACTION)
        script.add_action(OUTPUT, self.DRAW_BUTTON_2_ACTION)
        script.add_action(OUTPUT, self.DRAW_BUTTON_3_ACTION)
        script.add_action(OUTPUT, self.DRAW_DIALOG_ACTION)
        script.add_action(OUTPUT, self.END_DRAWING_ACTION)