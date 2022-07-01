import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0136_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0136   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '威诺'),
    TXT(0x02, '乘客'),
    TXT(0x03, '乘客'),
    TXT(0x04, '伊娜'),
    TXT(0x05, '安莉尔'),
    TXT(0x06, '小猫'),
    TXT(0x07, '小猫'),
    TXT(0x08, '小猫'),
    TXT(0x09, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0136.x'
    header.mapIndex       = 8
    header.bgm            = 84
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T0136_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xA99
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
        ('ED6_DT07/CH01560._CH', 'ED6_DT07/CH01560P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
        ('ED6_DT07/CH01470._CH', 'ED6_DT07/CH01470P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01700._CH', 'ED6_DT07/CH01700P._CP'),
        ('ED6_DT27/CH03880._CH', 'ED6_DT27/CH03880P._CP'),
        ('ED6_DT27/CH03881._CH', 'ED6_DT27/CH03881P._CP'),
        ('ED6_DT27/CH03882._CH', 'ED6_DT27/CH03882P._CP'),
    ]

# id: 0x10002 offset: 0xFA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 4500,
            z                   = 0,
            y                   = 190662,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = -46140,
            z                   = 0,
            y                   = 152120,
            direction           = 80,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = -48490,
            z                   = 0,
            y                   = 155900,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0111,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = -86540,
            z                   = 0,
            y                   = 119250,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = -85700,
            z                   = 0,
            y                   = 120430,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0195,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x1FA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x1FA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x1FA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 6598,
            triggerZ            = 0,
            triggerY            = 190158,
            triggerRange        = 1000,
            actorX              = 4500,
            actorZ              = 1500,
            actorY              = 190662,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 3130,
            triggerZ            = 0,
            triggerY            = 192000,
            triggerRange        = 800,
            actorX              = 3130,
            actorZ              = 1000,
            actorY              = 192000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x242
@scena.Code('PreInit')
def PreInit():
    ExecExpressionWithValue(
        0x000D,
        0x2D,
        (
            (Expr.PushLong, 0x258),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x2E,
        (
            (Expr.PushLong, 0x258),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x2F,
        (
            (Expr.PushLong, 0x258),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x07,
        (
            (Expr.PushLong, 0x258),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x29,
        (
            (Expr.PushLong, 0x258),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x2D,
        (
            (Expr.PushLong, 0x258),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x2E,
        (
            (Expr.PushLong, 0x258),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x2F,
        (
            (Expr.PushLong, 0x258),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x07,
        (
            (Expr.PushLong, 0x258),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x29,
        (
            (Expr.PushLong, 0x258),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x28,
        (
            (Expr.PushLong, 0x10),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x2D,
        (
            (Expr.PushLong, 0x258),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x2E,
        (
            (Expr.PushLong, 0x258),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x2F,
        (
            (Expr.PushLong, 0x258),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x07,
        (
            (Expr.PushLong, 0x258),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x29,
        (
            (Expr.PushLong, 0x258),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_300',
    )

    OP_A3(0x10F0)
    Event(1, 0x0003)

    def _loc_300(): pass

    label('loc_300')

    If(
        (
            (Expr.Eval, "OP_29(0x0074, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_386',
    )

    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    SetChrFlags(0x000C, 0x0040)
    SetChrFlags(0x000D, 0x0004)
    SetChrFlags(0x000E, 0x0004)
    SetChrPos(0x000B, -85600, 0, 119540, 0)
    SetChrPos(0x000F, -84190, 0, 123070, 330)
    SetChrPos(0x000E, -83500, 580, 117300, 270)
    SetChrPos(0x000D, -83030, 580, 116830, 315)
    CreateThread(0x000F, 0x01, 0x00, 0x0002)
    CreateThread(0x000E, 0x01, 0x00, 0x0003)
    CreateThread(0x000D, 0x01, 0x00, 0x0003)

    def _loc_386(): pass

    label('loc_386')

    Return()

# id: 0x0001 offset: 0x387
@scena.Code('Init')
def Init():
    OP_82(0x80, 0x00)
    OP_82(0x81, 0x00)
    OP_82(0x82, 0x00)

    Return()

# id: 0x0002 offset: 0x391
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3B4',
    )

    OP_8D(0x00FE, -85500, 124240, -83590, 123040, 1000)

    Jump('ReInit')

    def _loc_3B4(): pass

    label('loc_3B4')

    Return()

# id: 0x0003 offset: 0x3B5
@scena.Code('func_03_3B5')
def func_03_3B5():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3D8',
    )

    OP_8D(0x00FE, -83870, 117760, -83140, 116930, 1000)

    Jump('func_03_3B5')

    def _loc_3D8(): pass

    label('loc_3D8')

    Return()

# id: 0x0004 offset: 0x3D9
@scena.Code('func_04_3D9')
def func_04_3D9():
    ClearChrFlags(0x00FE, 0x0001)
    def _loc_3DE(): pass

    label('loc_3DE')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_438',
    )

    OP_8C(0x00FE, 270, 400)
    OP_8E(0x00FE, -84140, 4019, 122290, 1000, 0x00)
    OP_8C(0x00FE, 180, 400)
    Sleep(1000)

    OP_8C(0x00FE, 90, 400)
    OP_8E(0x00FE, -81450, 4019, 122290, 1000, 0x00)
    OP_8C(0x00FE, 180, 400)
    Sleep(1000)

    Jump('loc_3DE')

    def _loc_438(): pass

    label('loc_438')

    Return()

# id: 0x0005 offset: 0x439
@scena.Code('func_05_439')
def func_05_439():
    Call(0, 0x0006)

    Return()

# id: 0x0006 offset: 0x43E
@scena.Code('func_06_43E')
def func_06_43E():
    TalkBegin(0x0008)
    Call(6, 0x0006)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_45B',
    )

    OP_0D()
    OP_A9(0x05)
    OP_56(0x00)
    TalkEnd(0x0008)

    Return()

    def _loc_45B(): pass

    label('loc_45B')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_46C',
    )

    TalkEnd(0x0008)

    Return()

    def _loc_46C(): pass

    label('loc_46C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 2, 0x1812)),
            Expr.Return,
        ),
        'loc_6E8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0312, 7, 0x1897)),
            Expr.Return,
        ),
        'loc_56E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4FE',
    )

    ChrTalk(
        0x0008,
        (
            '到了晚上还没散，\n',
            '这真是一场麻烦的雾呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '呼，今晚也仍然要\n',
            '去提醒住客们关好门窗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '因为夜雾会让\n',
            '房间很潮湿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_56B')

    def _loc_4FE(): pass

    label('loc_4FE')

    ChrTalk(
        0x0008,
        (
            '那么，有什么事的话\n',
            '我会联络协会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不过到了晚上这雾\n',
            '居然还不散……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '它到底是从哪里\n',
            '涌来的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_56B(): pass

    label('loc_56B')

    Jump('loc_6E8')

    def _loc_56E(): pass

    label('loc_56E')

    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x0008, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '哟，这不是艾丝蒂尔小姐吗。\n',
            '还有雪拉扎德小姐…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '游击士的工作\n',
            '辛苦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1002F威诺先生。\n',
            '没什么怪事发生吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '是的，本旅馆\n',
            '非常地平静。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '……说来，莫非是有什么案件发生了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F我们巡逻只是为了保险起见，\n',
            '请别太担心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0103, 400)

    ChrTalk(
        0x0008,
        (
            '原来如此，是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '那么，有什么事的话\n',
            '我会联络协会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F嗯，拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1897)
    OP_A2(0x0000)

    def _loc_6E8(): pass

    label('loc_6E8')

    TalkEnd(0x0008)

    Return()

# id: 0x0007 offset: 0x6EC
@scena.Code('func_07_6EC')
def func_07_6EC():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 2, 0x1812)),
            Expr.Return,
        ),
        'loc_7B2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_740',
    )

    ChrTalk(
        0x00FE,
        (
            '好像很久没\n',
            '在外住宿了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难得有机会\n',
            '好好享受天伦之乐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7B2')

    def _loc_740(): pass

    label('loc_740')

    ChrTalk(
        0x00FE,
        (
            '也联络过妻子了，\n',
            '这样一来可以放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼～好像很久没\n',
            '在外住宿了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难得有机会\n',
            '好好享受天伦之乐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_7B2(): pass

    label('loc_7B2')

    TalkEnd(0x0009)

    Return()

# id: 0x0008 offset: 0x7B6
@scena.Code('func_08_7B6')
def func_08_7B6():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 2, 0x1812)),
            Expr.Return,
        ),
        'loc_802',
    )

    ChrTalk(
        0x00FE,
        (
            '啊～从这里可以\n',
            '看到定期船哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔～能不能\n',
            '快点动起来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_802(): pass

    label('loc_802')

    TalkEnd(0x000A)

    Return()

# id: 0x0009 offset: 0x806
@scena.Code('func_09_806')
def func_09_806():
    TalkBegin(0x000B)

    If(
        (
            (Expr.Eval, "OP_29(0x0074, 0x00, 0x02)"),
            Expr.Return,
        ),
        'loc_986',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0074, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_853',
    )

    ChrTalk(
        0x00FE,
        (
            '唔～什么样的\n',
            '名字最好呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '阿姨很烦恼啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_983')

    def _loc_853(): pass

    label('loc_853')

    If(
        (
            (Expr.Eval, "OP_29(0x0074, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_96D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_8B4',
    )

    ChrTalk(
        0x00FE,
        (
            '#1090461060V阿姨在这里等着哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1090461061V安莉尔\n',
            '就拜托你们了～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_96A')

    def _loc_8B4(): pass

    label('loc_8B4')

    ChrTalk(
        0x00FE,
        (
            '#1090461062V啊～各位游击士。\n',
            '找到安莉尔了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010461063V#1000F现在还在调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030461064V#020F找到了我们会回来通知的，\n',
            '请耐心等待。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1090461065V嗯～拜托了～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_96A(): pass

    label('loc_96A')

    Jump('loc_983')

    def _loc_96D(): pass

    label('loc_96D')

    If(
        (
            (Expr.Eval, "OP_29(0x0074, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_97F',
    )

    Call(1, 0x0001)

    Jump('loc_983')

    def _loc_97F(): pass

    label('loc_97F')

    Call(1, 0x0000)

    def _loc_983(): pass

    label('loc_983')

    Jump('loc_9EF')

    def _loc_986(): pass

    label('loc_986')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 2, 0x1812)),
            Expr.Return,
        ),
        'loc_9EF',
    )

    ChrTalk(
        0x00FE,
        (
            '#1090461066V真是的～\n',
            '外边一片雾蒙蒙的，啥都看不见了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1090461067V呼～这样\n',
            '是要迷路的～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9EF(): pass

    label('loc_9EF')

    TalkEnd(0x000B)

    Return()

# id: 0x000A offset: 0x9F3
@scena.Code('func_0A_9F3')
def func_0A_9F3():
    TalkBegin(0x000C)
    OP_22(0x0192, 0x00, 0x64)

    ChrTalk(
        0x00FE,
        (
            '喵～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000C)

    Return()

# id: 0x000B offset: 0xA0B
@scena.Code('func_0B_A0B')
def func_0B_A0B():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　　　　　　　工作人员室　　　　　　　\n',
            '          ※无关人员请勿入内',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
