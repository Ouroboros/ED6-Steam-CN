import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T2810_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2810   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2810.x'
    header.mapIndex       = 1
    header.bgm            = 84
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
        ('ED6_DT07/CH01663._CH', 'ED6_DT07/CH01663P._CP'),
        ('ED6_DT07/CH01213._CH', 'ED6_DT07/CH01213P._CP'),
        ('ED6_DT07/CH01433._CH', 'ED6_DT07/CH01433P._CP'),
        ('ED6_DT07/CH02603._CH', 'ED6_DT07/CH02603P._CP'),
        ('ED6_DT07/CH01360._CH', 'ED6_DT07/CH01360P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
    ]

# id: 0x10001 offset: 0xDA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '拉迪奥老师',
            x                   = 87640,
            z                   = 200,
            y                   = 2820,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0115,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '碧欧拉老师',
            x                   = 84430,
            z                   = 200,
            y                   = 1120,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0115,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '米丽亚老师',
            x                   = 84510,
            z                   = 200,
            y                   = 2890,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0115,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '科林兹校长',
            x                   = 116010,
            z                   = 200,
            y                   = 4800,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0115,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '亚吉鲁',
            x                   = 2540,
            z                   = 0,
            y                   = 33300,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '巴克斯',
            x                   = 2120,
            z                   = 0,
            y                   = 5500,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0002,
        ),
    )

# id: 0x10002 offset: 0x19A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x19A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x19A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 116010,
            triggerZ            = 0,
            triggerY            = 2750,
            triggerRange        = 400,
            actorX              = 116010,
            actorZ              = 1700,
            actorY              = 4800,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 51020,
            triggerZ            = 0,
            triggerY            = 31860,
            triggerRange        = 800,
            actorX              = 51020,
            actorZ              = 1500,
            actorY              = 31860,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1E2
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x1E3
@scena.Code('func_01_1E3')
def func_01_1E3():
    Return()

# id: 0x0002 offset: 0x1E4
@scena.Code('func_02_1E4')
def func_02_1E4():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_21C',
    )

    ChrTalk(
        0x00FE,
        (
            '这种时候要是碰上什么人\n',
            '肯定会吓一跳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25C')

    def _loc_21C(): pass

    label('loc_21C')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '哎呀，这样的夜晚\n',
            '来这里干什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我在检查门户呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_25C(): pass

    label('loc_25C')

    TalkEnd(0x00FE)

    Return()

# id: 0x0003 offset: 0x260
@scena.Code('func_03_260')
def func_03_260():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_2A4',
    )

    ChrTalk(
        0x00FE,
        (
            '好了，要是没事\n',
            '就赶快走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '别夺走我的孤独。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2EF')

    def _loc_2A4(): pass

    label('loc_2A4')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '呼呼呼……\n',
            '黑暗真令人安定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '果然，毫无人气的\n',
            '夜晚校舍最棒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2EF(): pass

    label('loc_2EF')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x2F3
@scena.Code('func_04_2F3')
def func_04_2F3():
    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0xB, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x05,
        (
            (Expr.GetChrWork, 0xB, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x000B)
    ChrClearFlags(0x000B, 0x0010)
    ChrTurnDirection(0x000B, 0x0000, 0)

    ExecExpressionWithValue(
        0x000B,
        0x04,
        (
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x04,
        (
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0xB, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x05,
        (
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_383',
    )

    Jump('loc_3C5')

    def _loc_383(): pass

    label('loc_383')

    If(
        (
            (Expr.GetChrWork, 0xB, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_39F',
    )

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3C5')

    def _loc_39F(): pass

    label('loc_39F')

    If(
        (
            (Expr.GetChrWork, 0xB, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_3BB',
    )

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3C5')

    def _loc_3BB(): pass

    label('loc_3BB')

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.GetChrWork, 0xB, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_3C5(): pass

    label('loc_3C5')

    ExecExpressionWithValue(
        0x000B,
        0x04,
        (
            (Expr.GetChrWork, 0x0, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x000B, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 2, 0x1222)),
            Expr.Return,
        ),
        'loc_691',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_447',
    )

    ChrTalk(
        0x000B,
        (
            '#0530211452V#780F旧校舍里可能\n',
            '潜伏着魔兽。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530211453V一定要小心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_691')

    def _loc_447(): pass

    label('loc_447')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x000B,
        (
            '#0530211445V#780F我问过老师了，\n',
            '据说你们准备前往旧校舍探索了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x000B, 0x0010)
    ChrTurnDirection(0x000B, 0x0105, 0)

    If(
        (
            (Expr.PushLong, 0x1E),
            (Expr.GetChrWork, 0xB, 0x4),
            Expr.Lss,
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0xA0),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4BB',
    )

    ChrSetSubChip(0x000B, 1)

    Jump('loc_4E1')

    def _loc_4BB(): pass

    label('loc_4BB')

    If(
        (
            (Expr.PushLong, 0xD2),
            (Expr.GetChrWork, 0xB, 0x4),
            Expr.Lss,
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x14A),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4DC',
    )

    ChrSetSubChip(0x000B, 2)

    Jump('loc_4E1')

    def _loc_4DC(): pass

    label('loc_4DC')

    ChrSetSubChip(0x000B, 0)

    def _loc_4E1(): pass

    label('loc_4E1')

    ChrSetDirection(0x000B, 180, 0)
    ChrSetFlags(0x000B, 0x0010)
    Sleep(200)

    ChrTalk(
        0x000B,
        (
            '#0530211446V#780F科洛丝、你也去吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211447V#040F是的，旧校舍的事\n',
            '我最清楚了，\n',
            '应该能帮上忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0530211448V#780F唔，原来如此。\n',
            '那样也好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x000B, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_5A4',
    )

    ChrTurnDirection(0x000B, 0x0103, 0)

    Jump('loc_5AB')

    def _loc_5A4(): pass

    label('loc_5A4')

    ChrTurnDirection(0x000B, 0x0106, 0)

    def _loc_5AB(): pass

    label('loc_5AB')

    If(
        (
            (Expr.PushLong, 0x1E),
            (Expr.GetChrWork, 0xB, 0x4),
            Expr.Lss,
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0xA0),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5CC',
    )

    ChrSetSubChip(0x000B, 1)

    Jump('loc_5F2')

    def _loc_5CC(): pass

    label('loc_5CC')

    If(
        (
            (Expr.PushLong, 0xD2),
            (Expr.GetChrWork, 0xB, 0x4),
            Expr.Lss,
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x14A),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5ED',
    )

    ChrSetSubChip(0x000B, 2)

    Jump('loc_5F2')

    def _loc_5ED(): pass

    label('loc_5ED')

    ChrSetSubChip(0x000B, 0)

    def _loc_5F2(): pass

    label('loc_5F2')

    ChrSetDirection(0x000B, 180, 0)
    ChrSetFlags(0x000B, 0x0010)
    Sleep(200)

    ChrTalk(
        0x000B,
        (
            '#0530211449V#780F那么各位、\n',
            '科洛丝就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_668',
    )

    ChrTalk(
        0x0103,
        (
            '#0030211450V#020F嗯嗯，交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_691')

    def _loc_668(): pass

    label('loc_668')

    ChrTalk(
        0x0106,
        (
            '#0050211451V#050F啊啊，交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_691(): pass

    label('loc_691')

    ChrSetSubChip(0x000B, 0)
    TalkEnd(0x000B)

    Return()

# id: 0x0005 offset: 0x69A
@scena.Code('func_05_69A')
def func_05_69A():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '这次我们班\n',
            '看来相当努力了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样就能赢过\n',
            '碧欧拉的班级了嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x6E9
@scena.Code('func_06_6E9')
def func_06_6E9():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '哼哼，我们班\n',
            '这次也干得不错呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '至少赢过米丽亚\n',
            '的班应该是毫无疑问的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x742
@scena.Code('func_07_742')
def func_07_742():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '呼～总算\n',
            '快打完分了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀，肩膀好硬。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x77A
@scena.Code('func_08_77A')
def func_08_77A():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　　走　\n',
            '　　廊　\n',
            '　　里　\n',
            '　　请　\n',
            '　　安　\n',
            '　学静　\n',
            '　生！　\n',
            '　指　　\n',
            '　导　　\n',
            '　部　　',
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
