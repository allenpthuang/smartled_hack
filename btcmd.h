#include <cstdint>

enum class HeaderPadding {
  PADDING_1 = 0x00,
  HEAD = 0xa5,
  PADDING_2 = 0xaa
};

enum class OnOff {
  ON  = 0xff,
  OFF = 0x00
};

enum class OpMode {
  PRESET = 0x00,
  MANUAL = 0x01,
  SOUND  = 0x04
};

enum class Preset {
  SEVEN_COLOR_FADE        = 0x00,
  RGB_FADE                = 0x01,
  SEVEN_COLOR_BREATHE     = 0x02,
  RGB_BREATHE             = 0x03,
  RED_AND_GREEN_FADE      = 0x04,
  RED_AND_BLUE_FADE       = 0x05,
  GREEN_AND_BLUE_FADE     = 0x06,
  SEVEN_COLOR_JUMP        = 0x07,
  RGB_JUMP                = 0x08,
  SEVEN_COLOR_FLASH       = 0x09,
  RGB_FLASH               = 0x0a,
  RED_FLASH               = 0x0b,
  GREEN_FLASH             = 0x0c,
  BLUE_FLASH              = 0x0d,
  YELLOW_FLASH            = 0x0e,
  PURPLE_FLASH            = 0x0f,
  CYAN_FLASH              = 0x10,
  WHITE_FLASH             = 0x11,
  YELLOW_AND_PURPLE_FLASH = 0x12,
  PURPLE_AND_CYAN         = 0x13
};

enum class MeteorPreset {
  SEVEN_COLOR_FADE        = 0x01,
  RGB_FADE                = 0x02,
  SEVEN_COLOR_BREATHE     = 0x03,
  RGB_BREATHE             = 0x04,
  RED_AND_GREEN_FADE      = 0x05,
  RED_AND_BLUE_FADE       = 0x06,
  GREEN_AND_BLUE_FADE     = 0x07,
  SEVEN_COLOR_JUMP        = 0x08,
  RGB_JUMP                = 0x09,
  SEVEN_COLOR_FLASH       = 0x0a,
  RGB_FLASH               = 0x0b,
  RED_FLASH               = 0x0c,
  GREEN_FLASH             = 0x0d,
  BLUE_FLASH              = 0x0e,
  YELLOW_FLASH            = 0x0f,
  PURPLE_FLASH            = 0x10,
  CYAN_FLASH              = 0x11,
  WHITE_FLASH             = 0x12,
  YELLOW_AND_PURPLE_FLASH = 0x13,
  PURPLE_AND_CYAN         = 0x14
};

class BTCmd {
 public:
  // Header
  HeaderPadding header : 8 = HeaderPadding::HEAD;

  // Power
  OnOff power : 8 = OnOff::ON; // off: 0x00; on: 0xff

  // Operation Mode
  OpMode opmode : 8 = OpMode::PRESET; // preset: 0x00; manual: 0x01; sound: 0x04

  // Preset
  Preset preset : 8 = Preset::SEVEN_COLOR_FADE; // 0x00 ~ 0x13 (0 - 19)
  int speed : 8 = 0x01; // 0x01 ~ 0x0a (1 - 10)

  // Manual Mode
  uint8_t red = 0xff;
  uint8_t green = 0xff;
  uint8_t blue = 0xff;
  // TODO(allenpthuang): check if it is in fact
  // `unit8 white = 0xff;`

  // Padding
  HeaderPadding padding_1 : 8 = HeaderPadding::PADDING_1;

  // Brightness
  int brightness : 8 = 0x01; // 0x01 ~ 0x64 (1 - 100)

  // Sound
  OnOff sound_onoff : 8 = OnOff::OFF; // off: 0x00; on: 0xff
  Preset sound_preset : 8 = Preset::SEVEN_COLOR_FADE; // 0x00 ~ 0x13 (0 - 19)
  int sound_sensitivity : 8 = 0x01; // 0x01 ~ 0x0a (1 - 10)

  // Twinkle
  OnOff twinkle_onoff : 8 = OnOff::OFF; // off: 0x00; on: 0xff
  int twinkle_speed : 8 = 0x01; // 0x01 ~ 0x04 (1 - 4)

  // Meteor
  OnOff meteor_onoff : 8 = OnOff::OFF; // off: 0x00; on: 0xff
  MeteorPreset meteor_preset : 8 = MeteorPreset::SEVEN_COLOR_FADE; // 0x01 ~ 0x14 (1 - 20)
  int meteor_speed : 8 = 0x01; // 0x01 ~ 0x04 (1 - 4)

  // Padding
  HeaderPadding padding_2 : 8 = HeaderPadding::PADDING_1;
  HeaderPadding padding_3 : 8 = HeaderPadding::PADDING_2;
};
