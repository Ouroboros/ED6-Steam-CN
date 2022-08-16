import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4310_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4310   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4310.x'
    header.mapIndex       = 1
    header.bgm            = 34
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
        ('ED6_DT27/CH03590._CH', 'ED6_DT27/CH03590P._CP'),
        ('ED6_DT07/CH01600._CH', 'ED6_DT07/CH01600P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
    ]

# id: 0x10001 offset: 0xC2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '希德中校',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '贝尔克副队长',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x162
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x162
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x162
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x162
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_175',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    Event(0, func_02_177)

    def _loc_175(): pass

    label('loc_175')

    Return()

# id: 0x0001 offset: 0x176
@scena.Code('func_01_176')
def func_01_176():
    Return()

# id: 0x0002 offset: 0x177
@scena.Code('func_02_177')
def func_02_177():
    EventBegin(0x00)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x0008, -80, 250, 68550, 180)
    ChrSetPos(0x0009, -1060, 250, 69080, 180)
    ChrSetPos(0x000A, 700, 0, 66610, 0)
    ChrSetPos(0x000B, -700, 0, 66610, 0)
    CameraMove(-50, 250, 68390, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(300, 0)
    FadeIn(1500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#2420270191V#2P现在在周游道的西北地区\n',
            '第１和第２小队已经展开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2420270192V#2P即将完成包围。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2430270193V#6P在东南地区有数名特务兵\n',
            '正在往罗马尔池的反方向更深处逃窜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2430270194V#6P第３和第４小队\n',
            '正在继续追击。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0620270195V#703F辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620270196V#700F维持现状，努力\n',
            '盯紧那两伙儿人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2P#1K是！',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x000B,
        (
            '#2430270198V#6P#1K是！',
            TxtCtl.Enter,
        ),
    )

    OP_56(0x01)
    OP_59()

    @scena.Lambda('lambda_0388')
    def lambda_0388():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0388)

    Sleep(100)

    @scena.Lambda('lambda_039B')
    def lambda_039B():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_039B)

    Sleep(500)

    @scena.Lambda('lambda_03AE')
    def lambda_03AE():
        CameraMove(-50, 250, 65390, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_03AE)

    @scena.Lambda('lambda_03C6')
    def lambda_03C6():
        ChrWalkTo(0x00FE, 700, 0, 52690, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_03C6)

    Sleep(50)

    @scena.Lambda('lambda_03E6')
    def lambda_03E6():
        ChrWalkTo(0x00FE, -700, 0, 52690, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_03E6)

    Sleep(3000)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_040B')
    def lambda_040B():
        CameraMove(-50, 250, 69390, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_040B)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_0428')
    def lambda_0428():
        ChrSetDirection(0x0009, 90, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0428)

    Sleep(400)

    ChrTalk(
        0x0009,
        (
            '#3170270199V#8P不过真是无法理解……\n',
            '他们到底在想什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3170270200V#8P难道是在声东击西？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_049E')
    def lambda_049E():
        ChrSetDirection(0x0008, 270, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_049E)

    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#0620270201V#703F#2P格兰赛尔配备有\n',
            '一个中队的兵力。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620270202V他们就算在这里拖住我们\n',
            '也不可能攻下王都。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620270203V#702F难道说他们手里有\n',
            '我们不知道的王牌……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3170270204V#8P王……牌？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, 0, 0, 60000, 0)

    ChrTalk(
        0x000C,
        (
            '#2440270205V#1P报告！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_05B5')
    def lambda_05B5():
        CameraMove(-50, 250, 68390, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_05B5)

    @scena.Lambda('lambda_05CD')
    def lambda_05CD():
        ChrSetDirection(0x0009, 180, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_05CD)

    Sleep(100)

    @scena.Lambda('lambda_05E0')
    def lambda_05E0():
        ChrSetDirection(0x0008, 180, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_05E0)

    ChrWalkTo(0x000C, 0, 0, 66610, 4000, 0x00)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#0620270206V#700F什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2440270207V已经和要塞司令部联络过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2440270208V不过跟游击士协会\n',
            '王都支部的联络……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2440270209V可能是出了什么问题，\n',
            '对方始终没有应答。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0620270210V#702F什么……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2440270211V您怎么认为？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0620270212V#700F嗯，让我想想……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620270213V#703F……以防万一，\n',
            '还是要下一道保险。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 270, 400)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0620270214V#700F#2P副队长，这里就交给你了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620270215V我去一下通讯室。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0009, 90, 400)

    ChrTalk(
        0x0009,
        (
            '#3170270216V#8P明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3170270217V#8P那么您是要联络哪边？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0620270218V#701F#2P再一次联络要塞司令部。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/T4150._SN', 103, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
