import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0200_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0200   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0200.x'
    header.mapIndex       = 12
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T0200_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
        ('ED6_DT07/CH02350._CH', 'ED6_DT07/CH02350P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT27/CH03870._CH', 'ED6_DT27/CH03870P._CP'),
        ('ED6_DT27/CH03871._CH', 'ED6_DT27/CH03871P._CP'),
        ('ED6_DT27/CH03005._CH', 'ED6_DT27/CH03005P._CP'),
        ('ED6_DT07/CH01770._CH', 'ED6_DT07/CH01770P._CP'),
        ('ED6_DT26/CH20311._CH', 'ED6_DT26/CH20311P._CP'),
    ]

# id: 0x10001 offset: 0xE2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '克劳斯市长',
            x                   = 8700,
            z                   = 3650,
            y                   = 2510,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '士兵库雷',
            x                   = 7070,
            z                   = 450,
            y                   = 1530,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '乌鸦',
            x                   = 7640,
            z                   = 0,
            y                   = 11140,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '基蒂',
            x                   = -4940,
            z                   = 0,
            y                   = 6680,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '洛连特市街区',
            x                   = -20690,
            z                   = 0,
            y                   = -180,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x182
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x182
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x182
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 8130,
            triggerZ            = 0,
            triggerY            = -13900,
            triggerRange        = 1000,
            actorX              = 8130,
            actorZ              = 2100,
            actorY              = -13700,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0000,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1A6
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1C1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 6, 0x2086)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1BE',
    )

    ChrClearFlags(0x000B, 0x0080)

    def _loc_1BE(): pass

    label('loc_1BE')

    Jump('loc_1D2')

    def _loc_1C1(): pass

    label('loc_1C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 7, 0x181F)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1D2',
    )

    ChrClearFlags(0x0008, 0x0080)

    def _loc_1D2(): pass

    label('loc_1D2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 7, 0x181F)),
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1E3',
    )

    ChrClearFlags(0x0009, 0x0080)

    def _loc_1E3(): pass

    label('loc_1E3')

    If(
        (
            (Expr.Eval, "OP_29(0x0072, 0x01, 0x4000)"),
            Expr.Return,
        ),
        'loc_1FA',
    )

    ChrClearFlags(0x000A, 0x0080)
    CreateThread(0x000A, 0x00, 0x00, func_03_299)

    def _loc_1FA(): pass

    label('loc_1FA')

    Return()

# id: 0x0001 offset: 0x1FB
@scena.Code('func_01_1FB')
def func_01_1FB():
    OP_16(0x02, 4000, -117000, -128000, 2293762)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_24D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_238',
    )

    MapSetFlags(0x00000010)
    OP_11(0xE6, 0xF0, 0xFF, 0, 60000, 0)

    Jump('loc_24D')

    def _loc_238(): pass

    label('loc_238')

    MapSetFlags(0x00000010)
    OP_11(0xE6, 0xF0, 0xFF, 0, 80000, 0)

    def _loc_24D(): pass

    label('loc_24D')

    OP_64(0x00, 0x0001)

    If(
        (
            (Expr.Eval, "OP_29(0x0077, 0x01, 0x0008)"),
            (Expr.Eval, "OP_29(0x0077, 0x01, 0x0020)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0077, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_271',
    )

    OP_65(0x00, 0x0001)

    def _loc_271(): pass

    label('loc_271')

    If(
        (
            (Expr.Eval, "OP_29(0x0072, 0x01, 0x4000)"),
            Expr.Return,
        ),
        'loc_282',
    )

    OP_26(347)
    OP_26(140)

    def _loc_282(): pass

    label('loc_282')

    Return()

# id: 0x0002 offset: 0x283
@scena.Code('func_02_283')
def func_02_283():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_298',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_283')

    def _loc_298(): pass

    label('loc_298')

    Return()

# id: 0x0003 offset: 0x299
@scena.Code('func_03_299')
def func_03_299():
    ExecExpressionWithValue(
        0x00FE,
        0x28,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x00FE, 0x0040)
    OP_8D(0x00FE, 5590, 13090, 9980, 9010, 0)

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            Expr.Rand,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2CD(): pass

    label('loc_2CD')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4A5',
    )

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0x960),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Gtr,
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0x960),
            Expr.Sub,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Lss,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0x960),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Gtr,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0x960),
            Expr.Sub,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_46E',
    )

    TerminateThread(0x00FE, 0x01)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_354',
    )

    @scena.Lambda('lambda_0338')
    def lambda_0338():
        OP_97(0x00FE, 10450, 17010, 360000, 7000, 0x0001)
        Yield()

        Jump('lambda_0338')

    DispatchAsync2(0x00FE, 0x0001, lambda_0338)

    Jump('loc_373')

    def _loc_354(): pass

    label('loc_354')

    @scena.Lambda('lambda_035A')
    def lambda_035A():
        OP_97(0x00FE, 10450, 17010, -360000, 7000, 0x0001)
        Yield()

        Jump('lambda_035A')

    DispatchAsync2(0x00FE, 0x0001, lambda_035A)

    def _loc_373(): pass

    label('loc_373')

    ChrSetChipByIndex(0x00FE, 2)
    ChrClearFlags(0x00FE, 0x0400)
    ChrSetFlags(0x00FE, 0x0004)
    PlaySE(347, 0x00, 0x64)
    PlaySE(140, 0x00, 0x64)
    def _loc_38C(): pass

    label('loc_38C')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3C4',
    )

    ExecExpressionWithValue(
        0x00FE,
        0x02,
        (
            (Expr.PushLong, 0xC8),
            Expr.Add2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x2),
            (Expr.PushLong, 0x2328),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_3BC',
    )

    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 2000)

    Jump('loc_3C4')

    def _loc_3BC(): pass

    label('loc_3BC')

    Sleep(15)

    Jump('loc_38C')

    def _loc_3C4(): pass

    label('loc_3C4')

    TerminateThread(0x00FE, 0x01)
    ChrSetFlags(0x00FE, 0x0080)
    ChrClearFlags(0x00FE, 0x0004)
    ChrSetPos(0x00FE, 7640, 0, 11140, 270)
    def _loc_3E3(): pass

    label('loc_3E3')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_46B',
    )

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0x4650),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Lss,
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0x4650),
            Expr.Sub,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Gtr,
            Expr.Or,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0x4650),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Lss,
            Expr.Or,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0x4650),
            Expr.Sub,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Gtr,
            Expr.Or,
            Expr.Return,
        ),
        'loc_463',
    )

    ChrClearFlags(0x00FE, 0x0080)
    ChrSetChipByIndex(0x00FE, 3)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 0)
    ChrClearFlags(0x00FE, 0x0004)
    OP_8D(0x00FE, 5590, 13090, 9980, 9010, 0)

    Jump('loc_46B')

    def _loc_463(): pass

    label('loc_463')

    Sleep(500)

    Jump('loc_3E3')

    def _loc_46B(): pass

    label('loc_46B')

    Jump('loc_4A2')

    def _loc_46E(): pass

    label('loc_46E')

    Sleep(100)

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x14),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4A2',
    )

    @scena.Lambda('lambda_048A')
    def lambda_048A():
        OP_8D(0x00FE, 5590, 13090, 9980, 9010, 1500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_048A)

    def _loc_4A2(): pass

    label('loc_4A2')

    Jump('loc_2CD')

    def _loc_4A5(): pass

    label('loc_4A5')

    Return()

# id: 0x0004 offset: 0x4A6
@scena.Code('func_04_4A6')
def func_04_4A6():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 6, 0x181E)),
            Expr.Return,
        ),
        'loc_5DA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_552',
    )

    ChrTalk(
        0x0008,
        (
            '#0341330008V#602F这里对艾丝蒂尔\n',
            '来说就像是自己家的院子一样吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0341330009V不过，还是不能\n',
            '掉以轻心啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0341330010V雾很浓，\n',
            '什么东西都看不清楚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5D7')

    def _loc_552(): pass

    label('loc_552')

    ChrTalk(
        0x0008,
        (
            '#0341330011V#602F雾确实比昨天\n',
            '更加浓了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0341330012V艾丝蒂尔你们去\n',
            '疏导市民避难吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0341330013V请将他们疏导\n',
            '到安全场所。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_5D7(): pass

    label('loc_5D7')

    Jump('loc_703')

    def _loc_5DA(): pass

    label('loc_5DA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_703',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_642',
    )

    ChrTalk(
        0x0008,
        (
            '#0341330011V#602F雾确实比昨天\n',
            '更加浓了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0341330014V要出城的话\n',
            '可一定要小心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_703')

    def _loc_642(): pass

    label('loc_642')

    ChrTalk(
        0x0008,
        (
            '#0341330015V#602F噢，是艾丝蒂尔吗。\n',
            '这么早就开始工作，真辛苦啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0341330011V雾确实比昨天\n',
            '更加浓了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0341330016V如果要出城的话\n',
            '一定要小心啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0341330010V雾很浓，\n',
            '什么东西都看不清楚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_703(): pass

    label('loc_703')

    TalkEnd(0x0008)

    Return()

# id: 0x0005 offset: 0x707
@scena.Code('func_05_707')
def func_05_707():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_812',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_77D',
    )

    ChrTalk(
        0x00FE,
        (
            '阿斯顿队长是个了不起的军人，\n',
            '但也有洛克那种部下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，我完全可以体会\n',
            '阿斯顿队长的辛劳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_80F')

    def _loc_77D(): pass

    label('loc_77D')

    ChrTalk(
        0x00FE,
        (
            '阿斯顿队长是个了不起的军人，\n',
            '但也有洛克那种部下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……真是的，身为士兵\n',
            '却完全没有自觉性。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，我完全可以体会\n',
            '阿斯顿队长的辛劳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_80F(): pass

    label('loc_80F')

    Jump('loc_86D')

    def _loc_812(): pass

    label('loc_812')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 7, 0x181F)),
            Expr.Return,
        ),
        'loc_86D',
    )

    ChrTalk(
        0x00FE,
        (
            '阿斯顿队长好像是个\n',
            '很优秀的人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听说原来他在王都部队，\n',
            '果然名不虚传啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_86D(): pass

    label('loc_86D')

    TalkEnd(0x0009)

    Return()

# id: 0x0006 offset: 0x871
@scena.Code('func_06_871')
def func_06_871():
    TalkBegin(0x000B)

    ChrTalk(
        0x00FE,
        (
            '有商品要\n',
            '送来市长的宅邸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然事情已经结束了，\n',
            '但院子很漂亮……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然必须要快回到店里去，\n',
            '但却不由自主的想多留一会儿呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000B)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
