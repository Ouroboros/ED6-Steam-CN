import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4134_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4134   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4134.x'
    header.mapIndex       = 1
    header.bgm            = 34
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
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

# id: 0x10000 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH01410._CH', 'ED6_DT07/CH01410P._CP'),
        ('ED6_DT07/CH01400._CH', 'ED6_DT07/CH01400P._CP'),
        ('ED6_DT07/CH01670._CH', 'ED6_DT07/CH01670P._CP'),
    ]

# id: 0x10001 offset: 0xC2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '修女艾伦',
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
            name                = '卡兰大主教',
            x                   = -50,
            z                   = 1000,
            y                   = 20410,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '利瓦尔牧师',
            x                   = 2870,
            z                   = 1000,
            y                   = 18870,
            direction           = 272,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '修女诺雅',
            x                   = -132010,
            z                   = 0,
            y                   = 6440,
            direction           = 340,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
    )

# id: 0x10002 offset: 0x142
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x142
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x142
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 200,
            triggerZ            = 1000,
            triggerY            = 17890,
            triggerRange        = 400,
            actorX              = -50,
            actorZ              = 2500,
            actorY              = 20410,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -74990,
            triggerZ            = 0,
            triggerY            = 66030,
            triggerRange        = 800,
            actorX              = -74990,
            actorZ              = 1000,
            actorY              = 66030,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x18A
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x18B
@scena.Code('func_01_18B')
def func_01_18B():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 2, 0x163A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_19C',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_19C(): pass

    label('loc_19C')

    Return()

# id: 0x0002 offset: 0x19D
@scena.Code('func_02_19D')
def func_02_19D():
    Call(0, 0x0003)

    Return()

# id: 0x0003 offset: 0x1A2
@scena.Code('func_03_1A2')
def func_03_1A2():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C8, 5, 0x1645)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3B1',
    )

    ChrTurnDirection(0x0009, 0x0109, 0)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '这不是凯文神父吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '半夜三更的，有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#1060F大主教，这附近\n',
            '有什么异样吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '不，没发生什么\n',
            '怪事啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0109, 0x0101, 400)

    ChrTalk(
        0x0109,
        (
            '#1063F呼，艾丝蒂尔。\n',
            '看来不在这一带……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0109, 400)

    ChrTalk(
        0x0101,
        (
            '#1002F嗯、嗯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0109, 0x0009, 400)
    ChrTurnDirection(0x0101, 0x0009, 400)

    ChrTalk(
        0x0009,
        (
            '对了，凯文神父，\n',
            '在那份报告中提及的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#1064F啊，不好意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1066F现在有点紧急情况，\n',
            '我正在赶时间。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '关于那件事的详细内容，\n',
            '我以后再向你汇报。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '唔，这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '那你就小心行事吧。\n',
            '愿你们走在正确的道路上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#1062F多谢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x02C8, 5, 0x1645))

    Jump('loc_3D4')

    def _loc_3B1(): pass

    label('loc_3B1')

    ChrTalk(
        0x0009,
        (
            '怎么了？\n',
            '你们不是在赶时间吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3D4(): pass

    label('loc_3D4')

    TalkEnd(0x0009)

    Return()

# id: 0x0004 offset: 0x3D8
@scena.Code('func_04_3D8')
def func_04_3D8():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '还要准备签字仪式，\n',
            '今天会开门到很晚哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有什么困扰吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x420
@scena.Code('func_05_420')
def func_05_420():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '……修女的一天\n',
            '始于祈祷，终于祈祷。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '早晚的祈祷都\n',
            '各要进行２小时哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，空之女神啊，\n',
            '今天也很顺利……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x49C
@scena.Code('func_06_49C')
def func_06_49C():
    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上着锁。',
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
