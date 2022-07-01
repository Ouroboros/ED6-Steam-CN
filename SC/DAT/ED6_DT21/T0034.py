import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0034_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0034   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '00130雪拉待机'),
    TXT(0x02, '00131雪拉移动'),
    TXT(0x03, '00132雪拉攻击'),
    TXT(0x04, '00133雪拉被弹开'),
    TXT(0x05, '00134雪拉倒下'),
    TXT(0x06, '00135雪拉魔法咏唱'),
    TXT(0x07, '00136雪拉魔法发射'),
    TXT(0x08, '00137雪拉胜利'),
    TXT(0x09, '00160提妲待机'),
    TXT(0x0A, '00161提妲移动'),
    TXT(0x0B, '00162提妲攻击'),
    TXT(0x0C, '00163提妲被弹开'),
    TXT(0x0D, '00164提妲倒下'),
    TXT(0x0E, '00165提妲魔法咏唱'),
    TXT(0x0F, '00166提妲魔法发射'),
    TXT(0x10, '00167提妲胜利'),
    TXT(0x11, '00140科洛丝待机'),
    TXT(0x12, '00141科洛丝移动'),
    TXT(0x13, '00142科洛丝攻击'),
    TXT(0x14, '00143科洛丝被弹开'),
    TXT(0x15, '00144科洛丝倒下'),
    TXT(0x16, '00145科洛丝魔法咏唱'),
    TXT(0x17, '00146科洛丝魔法发射'),
    TXT(0x18, '00147科洛丝胜利'),
    TXT(0x19, '00110约修亚待机'),
    TXT(0x1A, '00111约修亚移动'),
    TXT(0x1B, '00112约修亚攻击'),
    TXT(0x1C, '00113约修亚被弹开'),
    TXT(0x1D, '00114约修亚倒下'),
    TXT(0x1E, '00115约修亚魔法咏唱'),
    TXT(0x1F, '00116约修亚魔法发射'),
    TXT(0x20, '00117约修亚胜利'),
    TXT(0x21, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'map1'
    header.mapModel       = 'T0030.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xA2B
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00000000,
            dword_04        = 0x00000000,
            dword_08        = 0x00000000,
            word_0C         = 0x0004,
            word_0E         = 0x0005,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 315,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 0,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10001 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH00110._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT07/CH00111._CH', 'ED6_DT07/CH00111P._CP'),
        ('ED6_DT07/CH00112._CH', 'ED6_DT07/CH00112P._CP'),
        ('ED6_DT07/CH00113._CH', 'ED6_DT07/CH00113P._CP'),
        ('ED6_DT07/CH00114._CH', 'ED6_DT07/CH00114P._CP'),
        ('ED6_DT07/CH00115._CH', 'ED6_DT07/CH00115P._CP'),
        ('ED6_DT07/CH00116._CH', 'ED6_DT07/CH00116P._CP'),
        ('ED6_DT07/CH00117._CH', 'ED6_DT07/CH00117P._CP'),
        ('ED6_DT07/CH00113._CH', 'ED6_DT07/CH00113P._CP'),
        ('ED6_DT07/CH00113._CH', 'ED6_DT07/CH00113P._CP'),
        ('ED6_DT07/CH00113._CH', 'ED6_DT07/CH00113P._CP'),
        ('ED6_DT07/CH00113._CH', 'ED6_DT07/CH00113P._CP'),
        ('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP'),
        ('ED6_DT07/CH00121._CH', 'ED6_DT07/CH00121P._CP'),
        ('ED6_DT07/CH00122._CH', 'ED6_DT07/CH00122P._CP'),
        ('ED6_DT07/CH00123._CH', 'ED6_DT07/CH00123P._CP'),
        ('ED6_DT07/CH00124._CH', 'ED6_DT07/CH00124P._CP'),
        ('ED6_DT07/CH00125._CH', 'ED6_DT07/CH00125P._CP'),
        ('ED6_DT07/CH00126._CH', 'ED6_DT07/CH00126P._CP'),
        ('ED6_DT07/CH00127._CH', 'ED6_DT07/CH00127P._CP'),
        ('ED6_DT07/CH00123._CH', 'ED6_DT07/CH00123P._CP'),
        ('ED6_DT07/CH00123._CH', 'ED6_DT07/CH00123P._CP'),
        ('ED6_DT07/CH00123._CH', 'ED6_DT07/CH00123P._CP'),
        ('ED6_DT07/CH00123._CH', 'ED6_DT07/CH00123P._CP'),
        ('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP'),
        ('ED6_DT07/CH00161._CH', 'ED6_DT07/CH00161P._CP'),
        ('ED6_DT07/CH00162._CH', 'ED6_DT07/CH00162P._CP'),
        ('ED6_DT07/CH00163._CH', 'ED6_DT07/CH00163P._CP'),
        ('ED6_DT07/CH00164._CH', 'ED6_DT07/CH00164P._CP'),
        ('ED6_DT07/CH00165._CH', 'ED6_DT07/CH00165P._CP'),
        ('ED6_DT07/CH00166._CH', 'ED6_DT07/CH00166P._CP'),
        ('ED6_DT07/CH00167._CH', 'ED6_DT07/CH00167P._CP'),
        ('ED6_DT07/CH00163._CH', 'ED6_DT07/CH00163P._CP'),
        ('ED6_DT07/CH00163._CH', 'ED6_DT07/CH00163P._CP'),
        ('ED6_DT07/CH00163._CH', 'ED6_DT07/CH00163P._CP'),
        ('ED6_DT07/CH00163._CH', 'ED6_DT07/CH00163P._CP'),
        ('ED6_DT07/CH00140._CH', 'ED6_DT07/CH00140P._CP'),
        ('ED6_DT07/CH00141._CH', 'ED6_DT07/CH00141P._CP'),
        ('ED6_DT07/CH00142._CH', 'ED6_DT07/CH00142P._CP'),
        ('ED6_DT07/CH00143._CH', 'ED6_DT07/CH00143P._CP'),
        ('ED6_DT07/CH00144._CH', 'ED6_DT07/CH00144P._CP'),
        ('ED6_DT07/CH00145._CH', 'ED6_DT07/CH00145P._CP'),
        ('ED6_DT07/CH00146._CH', 'ED6_DT07/CH00146P._CP'),
        ('ED6_DT07/CH00147._CH', 'ED6_DT07/CH00147P._CP'),
        ('ED6_DT07/CH00143._CH', 'ED6_DT07/CH00143P._CP'),
        ('ED6_DT07/CH00143._CH', 'ED6_DT07/CH00143P._CP'),
        ('ED6_DT07/CH00143._CH', 'ED6_DT07/CH00143P._CP'),
        ('ED6_DT07/CH00143._CH', 'ED6_DT07/CH00143P._CP'),
    ]

# id: 0x10002 offset: 0x22A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 8000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            x                   = 8000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            x                   = 8000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000B,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            x                   = 8000,
            z                   = 0,
            y                   = 16000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            x                   = 8000,
            z                   = 0,
            y                   = 20000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            x                   = 8000,
            z                   = 0,
            y                   = 24000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000C,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            x                   = 8000,
            z                   = 0,
            y                   = 28000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000D,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            x                   = 8000,
            z                   = 0,
            y                   = 32000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000E,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            x                   = 12000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 24,
            chipIndex           = 24,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            x                   = 12000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 25,
            chipIndex           = 25,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            x                   = 12000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000F,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            x                   = 12000,
            z                   = 0,
            y                   = 16000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 27,
            chipIndex           = 27,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            x                   = 12000,
            z                   = 0,
            y                   = 20000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 28,
            chipIndex           = 28,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            x                   = 12000,
            z                   = 0,
            y                   = 24000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 29,
            chipIndex           = 29,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0010,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            x                   = 12000,
            z                   = 0,
            y                   = 28000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 30,
            chipIndex           = 30,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0011,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            x                   = 12000,
            z                   = 0,
            y                   = 32000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 31,
            chipIndex           = 31,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0012,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            x                   = 16000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 36,
            chipIndex           = 36,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            x                   = 16000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 37,
            chipIndex           = 37,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            x                   = 16000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 38,
            chipIndex           = 38,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0013,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            x                   = 16000,
            z                   = 0,
            y                   = 16000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 39,
            chipIndex           = 39,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            x                   = 16000,
            z                   = 0,
            y                   = 20000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 40,
            chipIndex           = 40,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            x                   = 16000,
            z                   = 0,
            y                   = 24000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 41,
            chipIndex           = 41,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0014,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            x                   = 16000,
            z                   = 0,
            y                   = 28000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 42,
            chipIndex           = 42,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0015,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            x                   = 16000,
            z                   = 0,
            y                   = 32000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 43,
            chipIndex           = 43,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0016,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            x                   = 24000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            x                   = 24000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            x                   = 24000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x001B,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            x                   = 24000,
            z                   = 0,
            y                   = 16000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            x                   = 24000,
            z                   = 0,
            y                   = 20000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            x                   = 24000,
            z                   = 0,
            y                   = 24000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x001C,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            x                   = 24000,
            z                   = 0,
            y                   = 28000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x001D,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            x                   = 24000,
            z                   = 0,
            y                   = 32000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x001E,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
    )

# id: 0x10003 offset: 0x62A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x62A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x62A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x62A
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x62B
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0x62C
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_641',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000708)

    Jump('ReInit')

    def _loc_641(): pass

    label('loc_641')

    Return()

# id: 0x0003 offset: 0x642
@scena.Code('func_03_642')
def func_03_642():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_657',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000007D0)

    Jump('func_03_642')

    def _loc_657(): pass

    label('loc_657')

    Return()

# id: 0x0004 offset: 0x658
@scena.Code('func_04_658')
def func_04_658():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_672',
    )

    OP_99(0x00FE, 0x00, 0x00, 0x000005DC)
    Sleep(500)

    Jump('func_04_658')

    def _loc_672(): pass

    label('loc_672')

    Return()

# id: 0x0005 offset: 0x673
@scena.Code('func_05_673')
def func_05_673():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_68D',
    )

    OP_99(0x00FE, 0x00, 0x03, 0x000007D0)
    Sleep(500)

    Jump('func_05_673')

    def _loc_68D(): pass

    label('loc_68D')

    Return()

# id: 0x0006 offset: 0x68E
@scena.Code('func_06_68E')
def func_06_68E():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_6A8',
    )

    OP_99(0x00FE, 0x00, 0x03, 0x000007D0)
    Sleep(500)

    Jump('func_06_68E')

    def _loc_6A8(): pass

    label('loc_6A8')

    Return()

# id: 0x0007 offset: 0x6A9
@scena.Code('func_07_6A9')
def func_07_6A9():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_6C3',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000007D0)
    Sleep(500)

    Jump('func_07_6A9')

    def _loc_6C3(): pass

    label('loc_6C3')

    Return()

# id: 0x0008 offset: 0x6C4
@scena.Code('func_08_6C4')
def func_08_6C4():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_6D9',
    )

    OP_99(0x00FE, 0x00, 0x03, 0x000004B0)

    Jump('func_08_6C4')

    def _loc_6D9(): pass

    label('loc_6D9')

    Return()

# id: 0x0009 offset: 0x6DA
@scena.Code('func_09_6DA')
def func_09_6DA():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_710',
    )

    SetChrChipByIndex(0x00FE, 5)
    OP_99(0x00FE, 0x00, 0x03, 0x000004B0)
    OP_99(0x00FE, 0x00, 0x03, 0x000004B0)
    SetChrChipByIndex(0x00FE, 6)
    OP_99(0x00FE, 0x00, 0x01, 0x000004B0)
    Sleep(1000)

    Jump('func_09_6DA')

    def _loc_710(): pass

    label('loc_710')

    Return()

# id: 0x000A offset: 0x711
@scena.Code('func_0A_711')
def func_0A_711():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_72B',
    )

    OP_99(0x00FE, 0x00, 0x0E, 0x000007D0)
    Sleep(500)

    Jump('func_0A_711')

    def _loc_72B(): pass

    label('loc_72B')

    Return()

# id: 0x000B offset: 0x72C
@scena.Code('func_0B_72C')
def func_0B_72C():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_746',
    )

    OP_99(0x00FE, 0x00, 0x09, 0x000007D0)
    Sleep(500)

    Jump('func_0B_72C')

    def _loc_746(): pass

    label('loc_746')

    Return()

# id: 0x000C offset: 0x747
@scena.Code('func_0C_747')
def func_0C_747():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_75C',
    )

    OP_99(0x00FE, 0x00, 0x03, 0x000004B0)

    Jump('func_0C_747')

    def _loc_75C(): pass

    label('loc_75C')

    Return()

# id: 0x000D offset: 0x75D
@scena.Code('func_0D_75D')
def func_0D_75D():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_793',
    )

    SetChrChipByIndex(0x00FE, 17)
    OP_99(0x00FE, 0x00, 0x03, 0x000004B0)
    OP_99(0x00FE, 0x00, 0x03, 0x000004B0)
    SetChrChipByIndex(0x00FE, 18)
    OP_99(0x00FE, 0x00, 0x01, 0x000004B0)
    Sleep(1000)

    Jump('func_0D_75D')

    def _loc_793(): pass

    label('loc_793')

    Return()

# id: 0x000E offset: 0x794
@scena.Code('func_0E_794')
def func_0E_794():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_7AE',
    )

    OP_99(0x00FE, 0x00, 0x0D, 0x000007D0)
    Sleep(500)

    Jump('func_0E_794')

    def _loc_7AE(): pass

    label('loc_7AE')

    Return()

# id: 0x000F offset: 0x7AF
@scena.Code('func_0F_7AF')
def func_0F_7AF():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_7C9',
    )

    OP_99(0x00FE, 0x00, 0x0D, 0x000007D0)
    Sleep(500)

    Jump('func_0F_7AF')

    def _loc_7C9(): pass

    label('loc_7C9')

    Return()

# id: 0x0010 offset: 0x7CA
@scena.Code('func_10_7CA')
def func_10_7CA():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_7DF',
    )

    OP_99(0x00FE, 0x00, 0x03, 0x000004B0)

    Jump('func_10_7CA')

    def _loc_7DF(): pass

    label('loc_7DF')

    Return()

# id: 0x0011 offset: 0x7E0
@scena.Code('func_11_7E0')
def func_11_7E0():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_816',
    )

    SetChrChipByIndex(0x00FE, 29)
    OP_99(0x00FE, 0x00, 0x03, 0x000004B0)
    OP_99(0x00FE, 0x00, 0x03, 0x000004B0)
    SetChrChipByIndex(0x00FE, 30)
    OP_99(0x00FE, 0x00, 0x01, 0x000004B0)
    Sleep(1000)

    Jump('func_11_7E0')

    def _loc_816(): pass

    label('loc_816')

    Return()

# id: 0x0012 offset: 0x817
@scena.Code('func_12_817')
def func_12_817():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_831',
    )

    OP_99(0x00FE, 0x00, 0x0E, 0x000003E8)
    Sleep(1000)

    Jump('func_12_817')

    def _loc_831(): pass

    label('loc_831')

    Return()

# id: 0x0013 offset: 0x832
@scena.Code('func_13_832')
def func_13_832():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_84C',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000007D0)
    Sleep(500)

    Jump('func_13_832')

    def _loc_84C(): pass

    label('loc_84C')

    Return()

# id: 0x0014 offset: 0x84D
@scena.Code('func_14_84D')
def func_14_84D():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_862',
    )

    OP_99(0x00FE, 0x00, 0x03, 0x000004B0)

    Jump('func_14_84D')

    def _loc_862(): pass

    label('loc_862')

    Return()

# id: 0x0015 offset: 0x863
@scena.Code('func_15_863')
def func_15_863():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_899',
    )

    SetChrChipByIndex(0x00FE, 41)
    OP_99(0x00FE, 0x00, 0x03, 0x000004B0)
    OP_99(0x00FE, 0x00, 0x03, 0x000004B0)
    SetChrChipByIndex(0x00FE, 42)
    OP_99(0x00FE, 0x00, 0x01, 0x000004B0)
    Sleep(1000)

    Jump('func_15_863')

    def _loc_899(): pass

    label('loc_899')

    Return()

# id: 0x0016 offset: 0x89A
@scena.Code('func_16_89A')
def func_16_89A():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_8B4',
    )

    OP_99(0x00FE, 0x00, 0x14, 0x000007D0)
    Sleep(500)

    Jump('func_16_89A')

    def _loc_8B4(): pass

    label('loc_8B4')

    Return()

# id: 0x0017 offset: 0x8B5
@scena.Code('func_17_8B5')
def func_17_8B5():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_8CF',
    )

    OP_99(0x00FE, 0x00, 0x0C, 0x000007D0)
    Sleep(500)

    Jump('func_17_8B5')

    def _loc_8CF(): pass

    label('loc_8CF')

    Return()

# id: 0x0018 offset: 0x8D0
@scena.Code('func_18_8D0')
def func_18_8D0():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_8E5',
    )

    OP_99(0x00FE, 0x00, 0x03, 0x000004B0)

    Jump('func_18_8D0')

    def _loc_8E5(): pass

    label('loc_8E5')

    Return()

# id: 0x0019 offset: 0x8E6
@scena.Code('func_19_8E6')
def func_19_8E6():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_91C',
    )

    SetChrChipByIndex(0x00FE, 53)
    OP_99(0x00FE, 0x00, 0x03, 0x000004B0)
    OP_99(0x00FE, 0x00, 0x03, 0x000004B0)
    SetChrChipByIndex(0x00FE, 54)
    OP_99(0x00FE, 0x00, 0x01, 0x000004B0)
    Sleep(1000)

    Jump('func_19_8E6')

    def _loc_91C(): pass

    label('loc_91C')

    Return()

# id: 0x001A offset: 0x91D
@scena.Code('func_1A_91D')
def func_1A_91D():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_937',
    )

    OP_99(0x00FE, 0x00, 0x13, 0x000007D0)
    Sleep(500)

    Jump('func_1A_91D')

    def _loc_937(): pass

    label('loc_937')

    Return()

# id: 0x001B offset: 0x938
@scena.Code('func_1B_938')
def func_1B_938():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_952',
    )

    OP_99(0x00FE, 0x00, 0x0C, 0x000007D0)
    Sleep(500)

    Jump('func_1B_938')

    def _loc_952(): pass

    label('loc_952')

    Return()

# id: 0x001C offset: 0x953
@scena.Code('func_1C_953')
def func_1C_953():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_968',
    )

    OP_99(0x00FE, 0x00, 0x03, 0x000004B0)

    Jump('func_1C_953')

    def _loc_968(): pass

    label('loc_968')

    Return()

# id: 0x001D offset: 0x969
@scena.Code('func_1D_969')
def func_1D_969():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_99F',
    )

    SetChrChipByIndex(0x00FE, 5)
    OP_99(0x00FE, 0x00, 0x03, 0x000004B0)
    OP_99(0x00FE, 0x00, 0x03, 0x000004B0)
    SetChrChipByIndex(0x00FE, 6)
    OP_99(0x00FE, 0x00, 0x01, 0x000004B0)
    Sleep(1000)

    Jump('func_1D_969')

    def _loc_99F(): pass

    label('loc_99F')

    Return()

# id: 0x001E offset: 0x9A0
@scena.Code('func_1E_9A0')
def func_1E_9A0():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_9BA',
    )

    OP_99(0x00FE, 0x00, 0x21, 0x000007D0)
    Sleep(500)

    Jump('func_1E_9A0')

    def _loc_9BA(): pass

    label('loc_9BA')

    Return()

# id: 0x001F offset: 0x9BB
@scena.Code('func_1F_9BB')
def func_1F_9BB():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_9D5',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000007D0)
    Sleep(500)

    Jump('func_1F_9BB')

    def _loc_9D5(): pass

    label('loc_9D5')

    Return()

# id: 0x0020 offset: 0x9D6
@scena.Code('func_20_9D6')
def func_20_9D6():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '呜喵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
