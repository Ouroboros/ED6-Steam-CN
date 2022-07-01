import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T1511_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1511   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '雪拉扎德'),
    TXT(0x02, '阿加特'),
    TXT(0x03, '奥利维尔'),
    TXT(0x04, '科洛丝'),
    TXT(0x05, '提妲'),
    TXT(0x06, '金'),
    TXT(0x07, '凯文神父'),
    TXT(0x08, '索菲娜'),
    TXT(0x09, '器皿'),
    TXT(0x0A, '器皿'),
    TXT(0x0B, '器皿'),
    TXT(0x0C, '器皿'),
    TXT(0x0D, '器皿'),
    TXT(0x0E, '器皿'),
    TXT(0x0F, '器皿'),
    TXT(0x10, '器皿'),
    TXT(0x11, '酒杯'),
    TXT(0x12, '酒杯'),
    TXT(0x13, '酒杯'),
    TXT(0x14, '酒杯'),
    TXT(0x15, '酒杯'),
    TXT(0x16, '酒杯'),
    TXT(0x17, '酒杯'),
    TXT(0x18, '酒杯'),
    TXT(0x19, '克鲁茨'),
    TXT(0x1A, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1511.x'
    header.mapIndex       = 1
    header.bgm            = 15
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x47A8
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
            dword_08        = 0x00001770,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 45,
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
        ('ED6_DT07/CH00023._CH', 'ED6_DT07/CH00023P._CP'),
        ('ED6_DT07/CH00053._CH', 'ED6_DT07/CH00053P._CP'),
        ('ED6_DT07/CH00033._CH', 'ED6_DT07/CH00033P._CP'),
        ('ED6_DT07/CH00043._CH', 'ED6_DT07/CH00043P._CP'),
        ('ED6_DT07/CH00063._CH', 'ED6_DT07/CH00063P._CP'),
        ('ED6_DT07/CH00073._CH', 'ED6_DT07/CH00073P._CP'),
        ('ED6_DT27/CH03083._CH', 'ED6_DT27/CH03083P._CP'),
        ('ED6_DT07/CH01690._CH', 'ED6_DT07/CH01690P._CP'),
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT07/CH00050._CH', 'ED6_DT07/CH00050P._CP'),
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT07/CH00040._CH', 'ED6_DT07/CH00040P._CP'),
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
        ('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP'),
        ('ED6_DT27/CH03080._CH', 'ED6_DT27/CH03080P._CP'),
        ('ED6_DT27/CH03003._CH', 'ED6_DT27/CH03003P._CP'),
        ('ED6_DT06/CH20020._CH', 'ED6_DT06/CH20020P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
        ('ED6_DT26/CH20403._CH', 'ED6_DT26/CH20403P._CP'),
        ('ED6_DT26/CH20373._CH', 'ED6_DT26/CH20373P._CP'),
    ]

# id: 0x10002 offset: 0x14A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 24500,
            z                   = 0,
            y                   = 6100,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 524304,
            chipIndex           = 16,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 524304,
            chipIndex           = 16,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 524304,
            chipIndex           = 16,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 524304,
            chipIndex           = 16,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 524304,
            chipIndex           = 16,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 524304,
            chipIndex           = 16,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 524304,
            chipIndex           = 16,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 524304,
            chipIndex           = 16,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 327697,
            chipIndex           = 17,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 327697,
            chipIndex           = 17,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 262161,
            chipIndex           = 17,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 327697,
            chipIndex           = 17,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 262161,
            chipIndex           = 17,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x46A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x46A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x46A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x46A
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_484',
    )

    OP_A3(0x10F0)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, 0x0002)

    Jump('loc_49B')

    def _loc_484(): pass

    label('loc_484')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_49B',
    )

    OP_A3(0x10F1)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, 0x0003)

    def _loc_49B(): pass

    label('loc_49B')

    Return()

# id: 0x0001 offset: 0x49C
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0x49D
@scena.Code('ReInit')
def ReInit():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4B0',
    )

    Call(0, 0x0004)

    def _loc_4B0(): pass

    label('loc_4B0')

    SetChrFlags(0x0101, 0x0004)
    SetChrPos(0x000E, 15900, 250, 11150, 180)
    SetChrPos(0x0101, 17150, 200, 9830, 270)
    SetChrPos(0x000B, 14800, 200, 9950, 90)
    SetChrPos(0x000C, 17300, 200, 8480, 270)
    SetChrPos(0x0008, 14840, 200, 8410, 90)
    SetChrPos(0x0009, 17340, 200, 6860, 270)
    SetChrPos(0x000A, 14850, 200, 6940, 90)
    SetChrPos(0x000D, 15940, 200, 5490, 0)
    SetChrChipByIndex(0x0101, 15)
    SetChrChipByIndex(0x0008, 0)
    SetChrChipByIndex(0x0009, 1)
    SetChrChipByIndex(0x000A, 2)
    SetChrChipByIndex(0x000B, 3)
    SetChrChipByIndex(0x000C, 4)
    SetChrChipByIndex(0x000D, 5)
    SetChrChipByIndex(0x000E, 6)
    SetChrSubChip(0x0101, 2)
    SetChrSubChip(0x0009, 2)
    SetChrSubChip(0x000C, 2)
    SetChrSubChip(0x0008, 1)
    SetChrSubChip(0x000A, 1)
    SetChrSubChip(0x000B, 1)
    SetChrSubChip(0x000D, 0)
    SetChrSubChip(0x000E, 0)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x0010, 15970, 800, 10210, 0)
    SetChrPos(0x0011, 16440, 800, 9370, 0)
    SetChrPos(0x0012, 15700, 800, 9540, 0)
    SetChrPos(0x0013, 16440, 800, 8109, 0)
    SetChrPos(0x0014, 15700, 800, 8390, 0)
    SetChrPos(0x0015, 16440, 800, 6900, 0)
    SetChrPos(0x0016, 15700, 800, 7140, 0)
    SetChrPos(0x0017, 15900, 800, 6260, 0)
    SetChrPos(0x0018, 15430, 800, 10100, 0)
    SetChrPos(0x0019, 16190, 800, 9880, 0)
    SetChrPos(0x001A, 15550, 800, 7940, 0)
    SetChrPos(0x001B, 15690, 800, 9110, 0)
    SetChrPos(0x001C, 16260, 800, 8610, 0)
    SetChrPos(0x001D, 16400, 800, 7350, 0)
    SetChrPos(0x001E, 15580, 800, 6670, 0)
    SetChrPos(0x001F, 16300, 800, 6360, 0)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x0017, 0x0080)
    ClearChrFlags(0x0018, 0x0080)
    ClearChrFlags(0x0019, 0x0080)
    ClearChrFlags(0x001A, 0x0080)
    ClearChrFlags(0x001B, 0x0080)
    ClearChrFlags(0x001C, 0x0080)
    ClearChrFlags(0x001D, 0x0080)
    ClearChrFlags(0x001E, 0x0080)
    ClearChrFlags(0x001F, 0x0080)
    OP_6D(16750, 200, 8800, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_6D(17040, 0, 9760, 0)
    OP_67(0, 6990, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_71(0x001D, 0x0004)
    OP_72(0x001E, 0x0004)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000E,
        (
            '#0180320542V#1065F#5P──原来如此。\n',
            '看来的确是件相当棘手的事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320543V真没想到传说中的古代龙\n',
            '竟然栖息在利贝尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320544V#1067F而且向人们警告了关于『辉之环』的事\n',
            '又不知道飞去了哪里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320545V#1007F#2P嗯，事情发生的太多\n',
            '感觉脑子都处理不过来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320546V#1015F而且不明白龙为什么\n',
            '对『辉之环』的事闭口不提。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0180320547V#1060F#5P其实，教会的圣典里\n',
            '有这样的记载……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320548V#1065F『授予至宝的女神，遣下圣兽\n',
            '见证人之子的未来。』',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0060320549V#043F#6P『至宝』和『圣兽』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060320550V看样子跟『辉之环』\n',
            '和『龙』的关系很相似呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040320551V#035F#6P而且『见证』这文字\n',
            '说不定是最为关键的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040320552V#030F看来龙的职责只能守望着大地，\n',
            '而不能插手进来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0050320553V#053F#2P呼，原来如此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0180320554V#1060F#5P无论如何，现在看来\n',
            '『辉之环』很可能是存在的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320555V结合我的种种调查\n',
            '可以做出各种推测……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320556V#1002F#2P凯文先生正在调查\n',
            '『四轮之塔』的事情吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320557V知道些什么了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0180320558V#1065F#5P算是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320559V#1063F关于４座塔顶上\n',
            '有不明用途的古代装置……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320560V你知道吗？它现在正在运作，\n',
            '并且还发出光亮。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C9A',
    )

    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【◇确认过装置还在运作】\n'),
            TXT(0x01, '【◇没确认过装置还在运作】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_C7C'),
        (0x00000001, 'loc_C8B'),
        (-1, 'loc_C9A'),
    )

    def _loc_C7C(): pass

    label('loc_C7C')

    OP_29(0x0066, 0x01, 0x1000)
    OP_29(0x0066, 0x01, 0x2000)

    Jump('loc_C9A')

    def _loc_C8B(): pass

    label('loc_C8B')

    OP_28(0x0066, 0x02, 0x1000)
    OP_28(0x0066, 0x02, 0x2000)

    Jump('loc_C9A')

    def _loc_C9A(): pass

    label('loc_C9A')

    If(
        (
            (Expr.Eval, "OP_29(0x0066, 0x01, 0x1000)"),
            (Expr.Eval, "OP_29(0x0066, 0x01, 0x2000)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_D0F',
    )

    ChrTalk(
        0x0101,
        (
            '#0010320561V#1015F#2P嗯，我们也\n',
            '亲眼确认过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320562V这和『辉之环』\n',
            '有什么关系吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D96')

    def _loc_D0F(): pass

    label('loc_D0F')

    ChrTalk(
        0x0101,
        (
            '#0010320563V#1004F#2P这么说来，在琥珀之塔\n',
            '剿灭魔兽的时候的确看到在发光呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320564V#1015F但是，这和『辉之环』\n',
            '有什么关系吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D96(): pass

    label('loc_D96')

    ChrTalk(
        0x000E,
        (
            '#0180320565V#1063F#5P尤莉亚上尉\n',
            '告诉过我……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320566V城里的『封印区域』最深处，\n',
            '巨大的机械化怪物出现之前\n',
            '曾经发生过奇怪的事情吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320567V#1004F#2P啊，嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320568V#1015F好像是在使用『福音』之后，\n',
            '遗迹的照明全部灭了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320569V然后就听到了警告的声音，\n',
            '周围的柱子都下降了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0030320570V#022F#6P警告内容是──『第１结界消灭』和\n',
            '『装置塔启动』吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0180320571V#1060F#5P对对，就是这个。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320572V#1065F然后，结合目击情报\n',
            '调查后我明白了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320573V#1063F４座塔的装置开始启动的时间\n',
            '正是在『封印区域』里\n',
            '使用『福音』的时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0008, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x000C, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000B, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x000A, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010320574V#1005F#2P你，你说什么～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0070320575V#065F#2P这，这么说，警告里说的\n',
            '『装置塔启动』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0080320576V#072F#4P就是指启动了\n',
            '『四轮之塔』塔顶的装置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0180320577V#1065F#5P嗯嗯，除此以外\n',
            '没有其他更合理的解释了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040320578V#035F#6P唔，把信息整理一下可以得出……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040320579V#030F格兰赛尔城的地下遗迹\n',
            '具备制造『第１结界』\n',
            '的机能。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040320580V但是，由于上校\n',
            '使用了『福音』，\n',
            '导致『第１结界』被消灭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0060320581V#047F#6P然后，取而代之的是\n',
            '『装置塔』开始启动了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060320582V#042F说不定\n',
            '是为了产生\n',
            '被称为『第２结界』的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320583V#1002F#2P『第２结界』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0050320584V#053F#2P哦，有第１\n',
            '就有第２，这倒也合情合理。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050320585V#552F问题是，这个所谓的结界\n',
            '到底是什么东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0180320586V#1065F#5P关于这个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320587V#1063F我想，结界的存在\n',
            '是为了隐藏『辉之环』的所在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    SetChrSubChip(0x0101, 2)
    Sleep(50)

    OP_62(0x0008, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    SetChrSubChip(0x0008, 1)
    Sleep(60)

    OP_62(0x000C, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    SetChrSubChip(0x000C, 2)
    Sleep(50)

    OP_62(0x000B, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    SetChrSubChip(0x000B, 1)
    Sleep(60)

    OP_62(0x0009, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    SetChrSubChip(0x0009, 2)
    Sleep(50)

    OP_62(0x000A, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    SetChrSubChip(0x000A, 1)
    Sleep(50)

    OP_62(0x000D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010320588V#1020F#2P是吗，『辉之环』\n',
            '不在封印区域里面……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320589V也就是说藏在\n',
            '利贝尔某处？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0180320590V#1060F#5P就是这么回事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320591V#1065F假设结社的目的\n',
            '是想得到『辉之环』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320592V#1063F那他们的『实验』\n',
            '就可以看成是\n',
            '为了达成这个目的所使用的手段吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320593V#1007F#2P嗯，嗯～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040320594V#035F#6P『辉之环』、『福音』……\n',
            '『结社酝酿的实验』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040320595V呵呵，看来一切\n',
            '都联系上了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040320596V#030F而描绘这张蓝图的\n',
            '就是那个被称为『教授』的人物吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0101, 0)
    Sleep(100)

    ChrTalk(
        0x0101,
        (
            '#0010320597V#1007F#2P嗯……是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320598V#1002F在龙的额头上埋入『福音』\n',
            '袭击柏斯各地的主谋……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320599V以及……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320600V#1003F…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0070320601V#064F#2P……姐姐？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x000E, 1)
    Sleep(100)

    ChrTalk(
        0x000E,
        (
            '#0180320602V#1064F#5P咋了，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x000B, 0)
    Sleep(100)

    ChrTalk(
        0x0101,
        (
            '#0010320603V#1007F#2P嗯……\n',
            '#1002F关于这个『教授』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320604V我认为约修亚的失踪\n',
            '有可能就是他一手造成的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0060320605V#043F#6P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0030320606V#022F#6P这么说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030320607V就是５年前，促成约修亚\n',
            '被老师收留的\n',
            '幕后黑手吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0101, 1)
    Sleep(100)

    ChrTalk(
        0x0101,
        (
            '#0010320608V#1003F#5P嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320609V#1010F还有，操纵理查德上校\n',
            '和克鲁茨前辈们记忆的人，\n',
            '我想也是那个教授。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0050320610V#052F#2P什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0080320611V#072F#4P喔，记忆操纵的事情确实\n',
            '尚未解明……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080320612V那你为什么会这么想？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320613V#1026F#5P嗯，这个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾斯蒂尔向大家说明了约修亚消失的那天傍晚，\n',
            '自己遇到过的人已经无法记起的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#0030320614V#022F#6P还有这种事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0050320615V#555F#2P你……\n',
            '一直隐瞒至今？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320616V#1025F#5P倒不是想故意要隐瞒什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320617V#1007F……抱歉，可能说得太晚了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0060320618V#042F#6P不过……\n',
            '看来没错了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060320619V我想那个人很可能\n',
            '就是各种事件的元凶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040320620V#032F#6P唔，看来是个性格\n',
            '相当冷酷的人物啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0080320621V#074F#4P啊啊……\n',
            '看来必须要多加注意了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0070320622V#063F#2P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320623V#1004F#5P对了……\n',
            '#1025F抱歉，提妲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320624V难得你来玩\n',
            '却说些这么扫兴的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0070320625V#560F#2P哪里……\n',
            '别在意，姐姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070320626V#561F我只是在想，为什么\n',
            '那个人要做这种事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070320627V让大家留下痛苦的回忆，\n',
            '又让约修亚哥哥受苦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070320628V我……真是不理解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320629V#1016F#5P好啦～那种性格扭曲的家伙\n',
            '没必要去理解啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320630V#1006F提妲走自己的路就对啦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320631V对吧，阿加特？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0050320632V#055F#2P我说啊～！\n',
            '为什么要问我啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x000B, 2)
    Sleep(100)

    ChrTalk(
        0x000B,
        (
            '#0060320633V#041F#6P嘻嘻……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0008, 0)
    Sleep(100)

    ChrTalk(
        0x0008,
        (
            '#0030320634V#027F#6P呵呵……\n',
            '这话问得还真是时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x000E, 0)
    Sleep(100)

    ChrTalk(
        0x000E,
        (
            '#0180320635V#1067F#5P…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0101, 0)
    Sleep(75)

    SetChrSubChip(0x0101, 2)
    Sleep(100)

    ChrTalk(
        0x0101,
        (
            '#0010320636V#1015F#2P嗯？\n',
            '怎么了，凯文先生？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x000B, 0)
    Sleep(75)

    SetChrSubChip(0x000B, 1)
    Sleep(100)

    ChrTalk(
        0x000E,
        (
            '#0180320637V#1060F#5P不……没什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320638V#1061F总而言之情报交换\n',
            '差不多就这样吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320639V来来来，难得这么美味的料理\n',
            '凉了可就不好吃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320640V#1006F#2P嗯，说得也是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x000B, 0)
    Sleep(50)

    SetChrSubChip(0x0101, 0)
    Sleep(50)

    SetChrSubChip(0x000C, 0)
    Sleep(50)

    SetChrSubChip(0x0009, 0)
    Sleep(100)

    ChrTalk(
        0x000A,
        (
            '#0040320641V#037F#6P呼，太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040320642V尽情享受\n',
            '美酒佳肴吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0008, 2)
    Sleep(100)

    OP_62(0x0008, 0x00000000, 1700, 0x0A, 0x0B, 0x000000FA, 0x02)
    OP_22(0x000F, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0030320643V#021F#5P哎呀，说啥呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 1700, 0x14, 0x17, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '#0040320644V#034F#4P……对不起。\n',
            '请原谅我的失礼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    OP_20(0x000005DC)
    OP_21()
    Sleep(500)

    OP_22(0x000D, 0x00, 0x64)
    Sleep(1500)

    Sleep(1500)

    Sleep(1500)

    Sleep(1500)

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '就这样……\n',
            '艾丝蒂尔等人享受了\n',
            '片刻的闲暇。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x10F1)
    NewScene('ED6_DT21/T1510._SN', 111, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x2162
@scena.Code('func_03_2162')
def func_03_2162():
    EventBegin(0x00)
    ClearChrFlags(0x0020, 0x0080)
    SetChrFlags(0x0020, 0x0004)
    SetChrFlags(0x0020, 0x0040)
    SetChrFlags(0x0020, 0x0002)
    SetChrPos(0x0020, 49000, -100, 22700, 180)
    SetChrChipByIndex(0x0020, 18)
    SetChrSubChip(0x0020, 0)
    OP_6F(0x001B, 11)
    SetChrFlags(0x000C, 0x0004)
    SetChrPos(0x0101, 50500, 0, 21820, 270)
    SetChrPos(0x000E, 50500, 0, 22640, 270)
    SetChrPos(0x0008, 50560, 0, 23630, 225)
    SetChrPos(0x000A, 50120, 0, 25120, 180)
    SetChrPos(0x0009, 48850, 0, 24330, 180)
    SetChrPos(0x000B, 51170, 0, 24660, 225)
    SetChrPos(0x000C, 49770, -100, 24140, 180)
    SetChrPos(0x000D, 48990, 0, 25290, 180)
    SetChrChipByIndex(0x0008, 8)
    SetChrChipByIndex(0x0009, 9)
    SetChrChipByIndex(0x000A, 10)
    SetChrChipByIndex(0x000B, 11)
    SetChrChipByIndex(0x000C, 12)
    SetChrChipByIndex(0x000D, 13)
    SetChrChipByIndex(0x000E, 14)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    OP_6D(51790, 0, 24790, 0)
    OP_67(0, 4970, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(54000, 0)
    OP_6E(294, 0)
    OP_6D(56510, 0, 29350, 0)
    OP_67(0, 4970, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(54000, 0)
    OP_6E(294, 0)

    @scena.Lambda('lambda_22ED')
    def lambda_22ED():
        OP_6D(51790, 0, 24790, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_22ED)

    FadeIn(1000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    ChrTalk(
        0x000E,
        (
            '#0180320807V#1065F#2P──虽然做了急救治疗，\n',
            '但伤势可不轻啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320808V#1063F暂时还是不要动比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320809V#1026F#2P是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0050320810V#552F#5P没想到克鲁茨这家伙\n',
            '竟然会被打成这样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050320811V到底发生了什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320812V#1002F#2P我记得克鲁茨前辈说过，\n',
            '他们的队伍好象已经找到\n',
            '结社的据点了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320813V这么说，亚妮拉丝\n',
            '和卡露娜前辈应该也在一起……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320814V#1020F啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0080320815V#572F#5P……糟了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0030320816V#022F#5P已经用房间里的通信器\n',
            '和卢格兰爷爷联络过了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030320817V应该也会很快\n',
            '和各地的协会和王国军取得联络的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320818V#1020F#2P但，但是……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320819V搞不好\n',
            '亚妮拉丝他们会……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0030320820V#020F#5P嗯嗯……我明白的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0050320821V#053F#5P我们最好也\n',
            '想办法行动吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050320822V#555F问题是载着克鲁茨的小船\n',
            '是从哪里漂来的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040320823V#032F#5P唔，记得瓦雷利亚湖里\n',
            '并没有岛屿或礁石吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0060320824V#043F#5P是的，因为水很深很深……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040320825V#035F#5P那么就必定是从\n',
            '某处湖岸漂来的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040320826V但是要确定这个地点\n',
            '不是件容易的事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320827V#1007F#2P嗯……\n',
            '这湖又那么大。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320828V#1015F要是能拜托军用警备艇\n',
            '参加搜索就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#0330320829V#847F呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x000E, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x000C, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000D, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010320830V#1004F#2P克鲁茨前辈！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    SetChrSubChip(0x0020, 1)
    Sleep(300)

    SetChrSubChip(0x0020, 2)
    Sleep(1500)

    SetChrSubChip(0x0020, 3)
    Sleep(1000)

    ChrTalk(
        0x0020,
        (
            '#0330320831V#844F这……这里是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330320832V艾丝蒂尔……\n',
            '……还有阿加特你们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0050320833V#556F#5P这里是柏斯地方南部，\n',
            '湖畔的『川蝉亭』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050320834V你乘上小船\n',
            '被漂到这里来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#0330320835V#844F是……是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330320836V#843F我记得和其他的队员\n',
            '潜入了『结社』据点……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330320837V…………然后……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0020, 0xFFFFFE70, 1800, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(2000)

    ChrTalk(
        0x0101,
        (
            '#0010320838V#1020F#2P克，克鲁茨前辈……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0030320839V#023F#5P难不成……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x0020)
    Sleep(500)

    ChrTalk(
        0x0020,
        (
            '#0330320840V#844F唔……怎么搞的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330320841V竟然连续两次……\n',
            '被夺去记忆……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320842V#1002F#2P果，果然……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040320843V#032F#5P看来被那什么『教授』\n',
            '封印了记忆啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0020, 2)
    Sleep(500)

    ChrTalk(
        0x0020,
        (
            '#0330320844V#842F拜，拜托……金先生！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330320845V就像以前那样，\n',
            '把『气』打到我身上……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330320846V不然这样下去的话，库拉茨他们会……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0080320847V#572F#5P……那仅仅是\n',
            '一种对症疗法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080320848V应该是没法恢复\n',
            '因暗示而被封印的记忆。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080320849V#074F而且，对现在有伤在身的你来说\n',
            '负担太重了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#0330320850V#844F但，但是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0180320851V#1060F#2P……这样的话\n',
            '我来想想办法吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0020, 0xFFFFFED4, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x000C, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x000D, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(500)

    @scena.Lambda('lambda_2DA6')
    def lambda_2DA6():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2DA6)

    @scena.Lambda('lambda_2DB4')
    def lambda_2DB4():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2DB4)

    Sleep(100)

    @scena.Lambda('lambda_2DC7')
    def lambda_2DC7():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2DC7)

    @scena.Lambda('lambda_2DD5')
    def lambda_2DD5():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_2DD5)

    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010320852V#1004F#2P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0020, 3)
    Sleep(500)

    ChrTalk(
        0x0020,
        (
            '#0330320853V#842F……你是……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0180320854V#1060F#2P我是七耀教会『星杯骑士』，\n',
            '凯文·格拉汉姆。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320855V亚妮拉丝他们\n',
            '没告诉过你吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#0330320856V#841F噢……是你……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320857V#1015F#2P但，但是，凯文先生。\n',
            '你能解除暗示吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0180320858V#1071F#2P嗯～如果已经深入到深层心理\n',
            '那就完全没有办法了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320859V不过若是解放暂时封印的记忆，\n',
            '应该能有办法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320860V#1062F而且，似乎被暗示\n',
            '的时间也不是很久。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320861V#1025F#2P是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040320862V#032F#5P唔，难道是所谓的教会流传的\n',
            '秘藏法术吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0180320863V#1061F#2P嗯，算是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320864V#1060F不过，精神上可能\n',
            '多少会受点伤害……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320865V这样也没关系吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#0330320866V#842F没问题……\n',
            '务必请您一试。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0180320867V#1065F#2P明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000003E8)
    OP_21()
    Fade(500)
    SetChrChipByIndex(0x000E, 19)
    SetChrSubChip(0x000E, 0)
    OP_21()
    Sleep(500)

    OP_22(0x00D8, 0x00, 0x64)
    SetChrSubChip(0x000E, 1)
    Sleep(1000)

    ChrTalk(
        0x000E,
        (
            '#0180320868V#1063F#2P──空之女神名下\n',
            '谨此圣化七耀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    OP_1D(0x21)
    Sleep(500)

    @scena.Lambda('lambda_316D')
    def lambda_316D():
        OP_6B(2600, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_316D)

    @scena.Lambda('lambda_317D')
    def lambda_317D():
        OP_8C(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_317D)

    @scena.Lambda('lambda_318B')
    def lambda_318B():
        OP_8C(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_318B)

    Sleep(50)

    @scena.Lambda('lambda_319E')
    def lambda_319E():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_319E)

    @scena.Lambda('lambda_31AC')
    def lambda_31AC():
        OP_8C(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_31AC)

    Sleep(500)

    LoadEffect(0x01, 'map\\\\mp082_00.eff')
    PlayEffect(0x01, 0x00, 0x000E, -450, 800, 400, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x00C9, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010320869V#1004F#2P（哇哇……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0070320870V#560F#5P（哇，好漂亮……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0180320871V#1065F#2P识之银耀，时之黒耀──',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320872V以其相克之力\n',
            '在此除却\n',
            '嵌入此人之楔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    LoadEffect(0x00, 'scraft\\\\sc008_02.eff')
    PlayEffect(0x00, 0xFF, 0x00FF, 50020, 900, 22900, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_23(0x00C9)
    OP_82(0x00, 0x02)
    Sleep(2000)

    SetChrSubChip(0x0020, 3)
    Sleep(100)

    SetChrSubChip(0x0020, 4)
    Sleep(100)

    SetChrSubChip(0x0020, 5)

    ChrTalk(
        0x0020,
        (
            '#0330320873V#847F……呜……！',
            TxtCtl.Enter,
        ),
    )

    OP_9E(0x0020, 0x00000014, 0x00000000, 0x000001F4, 0x00000BB8)
    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320874V#1020F#2P没事吧，克鲁茨前辈！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#0330320875V#847F啊啊……没事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330320876V……………………………\n',
            '……好像迷雾散去一般\n',
            '想起了……很多事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x000E, 14)
    SetChrSubChip(0x000E, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000E,
        (
            '#0180320877V#1063F#2P虽然迷雾已经散去，\n',
            '但还请慢慢让自己的心平静下来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320878V千万不可急于窥视\n',
            '那彼岸的黑暗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#0330320879V#843F啊啊……我明白。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330320880V呵呵，我明白所谓精神上的伤害\n',
            '是指什么了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330320881V那就是……正反面的自我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0180320882V#1064F#2P哎呀，你明白了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#0330320883V#843F别看我现在这样，\n',
            '也是修练过冥想的人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330320884V……………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0020, 5)
    Sleep(300)

    SetChrSubChip(0x0020, 4)
    Sleep(300)

    SetChrSubChip(0x0020, 3)
    Sleep(1000)

    ChrTalk(
        0x0020,
        (
            '#0330320885V#845F……已经没事了。\n',
            '我什么都想起来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320886V#1025F#2P真，真的！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0080320887V#070F#5P唔……真是高超的法术。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0050320888V#051F#5P呼，看来你不仅仅是个\n',
            '不良神父那么简单嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0030320889V#021F#5P呵呵……\n',
            '干得好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0180320890V#1061F#2P啊哈哈，没什么大不了的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320891V#1063F那么克鲁茨先生。\n',
            '你能想起来些什么吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#0330320892V#843F啊啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330320893V#842F『结社』的据点在\n',
            '瓦雷利亚湖西北的湖岸……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330320894V那里有他们秘密建造\n',
            '的研究设施……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320895V#1020F#2P研，研究设施！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0030320896V#022F#5P这东西究竟是什么时候……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0060320897V#043F#5P说到瓦雷利亚湖西北岸，\n',
            '确实是远离都市的地方……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060320898V不过应该也有\n',
            '警备艇在搜索啊……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#0330320899V#843F他们好像用特殊的方法\n',
            '隐藏了设施所在……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330320900V似乎是在上空播放伪装影像\n',
            '来防御空中搜索……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010261088V#1005F#2P你，你说什么～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040320902V#034F#5P这真是……\n',
            '让人无法理解的技术啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0070320903V#065F#5P原，原理上来说是可能的，\n',
            '但还是有点难以置信……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#0330320904V#844F而且在地面上……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330320905V一旦接近，似乎周围\n',
            '就会产生浓雾……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0060320906V#042F#5P雾……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0050320907V#552F#5P令人联想到洛连特的事件啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#0330320908V#843F我们的队伍穿过浓雾\n',
            '潜入了研究设施……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330320909V但遭到名为『执行者』的\n',
            '厉害人物的埋伏……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330320910V#844F我们完全被抓住了破绽，\n',
            '全线溃退……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330320911V刚逃到船上\n',
            '我就失去了意识……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330320912V#847F呜，没想到居然抛下了同伴\n',
            '独自逃生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320913V#1006F#2P克鲁茨前辈……放心吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320914V我们一定会把亚妮拉丝他们\n',
            '救出来的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#0330320915V#842F艾，艾丝蒂尔……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0050320916V#051F#5P噢，既然已经掌握了这么多情报，\n',
            '我们总能做点什么吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0030320917V#020F#5P是啊。\n',
            '而且军队也应该会派出支援。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0080320918V#070F#5P之后就交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#0330320919V#845F谢，谢谢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330320920V#847F抱歉……拜托你们了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0020, 4)
    Sleep(300)

    SetChrSubChip(0x0020, 5)
    Sleep(200)

    SetChrSubChip(0x0020, 6)
    Sleep(200)

    SetChrSubChip(0x0020, 7)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010270408V#1020F#2P怎，怎么了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0180320922V#1065F#2P没事，只是昏过去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320923V#1063F但是……\n',
            '看来已经没有时间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320924V#1005F#2P嗯……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320925V在王国军行动之前\n',
            '我们也必须采取行动才行！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)
    ChrTurnDirection(0x000B, 0x0101, 400)
    Sleep(200)

    ChrTalk(
        0x0008,
        (
            '#0030320926V#022F#5P艾丝蒂尔，我想不说\n',
            '你应该也知道……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000E, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010320927V#1003F#4P嗯……我明白。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320928V和之前的任务相比\n',
            '这次的危险程度完全不同对吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320929V#1002F不过，总有一天会\n',
            '以这种形式和『结社』对决，\n',
            '这我早有心理准备……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320930V只不过是提前了点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0030320931V#023F#5P艾丝蒂尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030320932V#524F呵呵，真是短暂的休假呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0050320933V#051F#5P喔，足够了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050320934V该下定决心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0080320935V#074F#5P但是，大家一起潜入\n',
            '反而会更显眼。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080320936V#070F我们还是精简一下人数吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320937V#1006F#4P嗯……也是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320938V#1015F对了，各位。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320939V就跟那时一样……\n',
            '也让我来选可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0030320940V#020F#5P那时是说……\n',
            '探索封印区域的时候吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0080320941V#070F#5P啊啊，没问题吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0050320942V#051F#5P嗯，就算没选我\n',
            '我也不会恨你啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040320943V#031F#5P呼，我确信\n',
            '一定会选到我的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0060320944V#048F#5P如果需要人负责回复，\n',
            '请务必带上我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0070320945V#062F#5P我，我对机械的事\n',
            '也一定能帮上忙的……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320946V#1025F#4P大家……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000E, 0x0101, 400)

    ChrTalk(
        0x000E,
        (
            '#0180320947V#1068F#5P啊～抱歉打个岔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320948V#1060F先把我选进队伍\n',
            '怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320949V#1004F#4P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0180320950V#1063F#5P看来亚妮拉丝他们\n',
            '已经落入『结社』手中了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320951V解救的时候，要是他们也被\n',
            '施了刚才那种法术该怎么办？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320952V#1020F#4P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0080320953V#070F#5P原来如此，有道理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0050320954V#051F#5P没办法……\n',
            '你就确定入选了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0180320955V#1061F#5P嘿嘿，多谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320956V#1016F#4P真是的，要说谢谢的\n',
            '是我才对啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320957V#1006F那么……\n',
            '来选剩下的队员吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A3(0x0000)
    def _loc_4459(): pass

    label('loc_4459')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_468C',
    )

    FadeOut(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            TxtCtl.ShowAll,
            0x18,
            (TxtCtl.SetColor, 0x5),
            '※进行队伍的重新编组。\n',
            '　更换队员，进行必要的装备变更，\n',
            '　确定后，请选择【继续】。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【编成队伍】\n'),
            TXT(0x01, '【变更装备】\n'),
            TXT(0x02, '【继续】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)
    OP_56(0x00)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_458D',
    )

    OP_A2(0x0000)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※进行队伍的重新编组。\n',
            '　请选择２名固定成员以外的同行者。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Sleep(100)

    OP_C9(
        0x00,
        (
            0x0000,
            0x0008,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0002,
            0x0006,
            0x0003,
            0x0004,
            0x0007,
            0xFFFF,
        ),
    )

    Jump('loc_4689')

    def _loc_458D(): pass

    label('loc_458D')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_45F4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_45C6',
    )

    OP_C0(0x13, 0x00000078, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)

    Jump('loc_45F1')

    def _loc_45C6(): pass

    label('loc_45C6')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※进行队伍的编组之后再选择。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Sleep(100)

    def _loc_45F1(): pass

    label('loc_45F1')

    Jump('loc_4689')

    def _loc_45F4(): pass

    label('loc_45F4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_465E',
    )

    SetChrName('')

    Talk(
        (
            TxtCtl.ShowAll,
            0x18,
            (TxtCtl.SetColor, 0x5),
            '※可以继续剧情了吗？',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【是】\n'),
            TXT(0x01, '【否】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)
    OP_56(0x00)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_465B',
    )

    Jump('loc_468C')

    def _loc_465B(): pass

    label('loc_465B')

    Jump('loc_4689')

    def _loc_465E(): pass

    label('loc_465E')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※进行队伍的编组之后再选择。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Sleep(100)

    def _loc_4689(): pass

    label('loc_4689')

    Jump('loc_4459')

    def _loc_468C(): pass

    label('loc_468C')

    OP_69(0x0000, 0x00000000)
    SetMapFlags(0x00000001)
    OP_20(0x00000BB8)
    OP_21()
    Sleep(1000)

    SetChrStatus(0x00FF, 0xFE, 0)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/E0901._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0x46B5
@scena.Code('func_04_46B5')
def func_04_46B5():
    FadeOut(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x09, 0xFF)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【◇选择雪拉扎德为队友】\n'),
            TXT(0x01, '【◇选择阿加特为队友】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_4732'),
        (0x00000001, 'loc_4738'),
        (-1, 'loc_473E'),
    )

    def _loc_4732(): pass

    label('loc_4732')

    OP_A2(0x1200)

    Jump('loc_473E')

    def _loc_4738(): pass

    label('loc_4738')

    OP_A2(0x1201)

    Jump('loc_473E')

    def _loc_473E(): pass

    label('loc_473E')

    Return()

# id: 0x0005 offset: 0x473F
@scena.Code('func_05_473F')
def func_05_473F():
    ClearMapFlags(0x00000001)
    OP_6D(64510, 0, -14780, 92)
    Sleep(100)

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            0x0000,
            0x00FF,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0002,
            0x0006,
            0x0003,
            0x0004,
            0x0007,
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0x00000000)
    Sleep(1000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
