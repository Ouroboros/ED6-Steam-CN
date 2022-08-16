import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T5101_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T5101   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'T5101.x'
    header.mapIndex       = 1
    header.bgm            = 84
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
        ('ED6_DT07/CH01620._CH', 'ED6_DT07/CH01620P._CP'),
    ]

# id: 0x10001 offset: 0xB2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '克鲁茨',
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
            name                = '目标用照相机',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0080,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0xF2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xF2
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -4320,
            y           = 0,
            z           = -36940,
            range       = 3430,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFF7338,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000003,
        ),
    )

# id: 0x10004 offset: 0x112
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -3550,
            triggerZ            = 0,
            triggerY            = -3000,
            triggerRange        = 800,
            actorX              = -4250,
            actorZ              = 1000,
            actorY              = -3000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x136
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0201, 3, 0x100B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_142',
    )

    Event(0, func_02_15B)

    def _loc_142(): pass

    label('loc_142')

    Return()

# id: 0x0001 offset: 0x143
@scena.Code('func_01_143')
def func_01_143():
    OP_16(0x02, 4000, -126000, -138000, 2293871)
    PlaySE(451, 0x00, 0x64)

    Return()

# id: 0x0002 offset: 0x15B
@scena.Code('func_02_15B')
def func_02_15B():
    EventBegin(0x00)
    MapClearFlags(0x00000001)
    CameraMove(5450, 0, 52290, 0)
    OP_67(0, 12830, -10000, 0)
    CameraSetDistance(4830, 0)
    OP_6C(325000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0008, -1740, 0, -20510, 356)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0101, -2300, 0, -22520, 70)
    ChrSetPos(0x010A, -650, 0, -22430, 342)

    @scena.Lambda('lambda_01DD')
    def lambda_01DD():
        CameraMove(-5130, 0, 1290, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_01DD)

    @scena.Lambda('lambda_01F5')
    def lambda_01F5():
        OP_67(0, 12830, -10000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_01F5)

    @scena.Lambda('lambda_020D')
    def lambda_020D():
        OP_6C(315000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_020D)

    Sleep(4000)

    @scena.Lambda('lambda_0222')
    def lambda_0222():
        ChrWalkTo(0x0008, -1810, 0, -70, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0222)

    Sleep(200)

    @scena.Lambda('lambda_0242')
    def lambda_0242():
        ChrWalkTo(0x0101, -2060, 0, -2530, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0242)

    Sleep(100)

    @scena.Lambda('lambda_0262')
    def lambda_0262():
        ChrWalkTo(0x010A, -1010, 0, -2530, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x010A, 0x0000, lambda_0262)

    WaitForThreadExit(0x0101, 0x0001)
    Fade(500)
    CameraMove(-1960, 0, -1210, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2900, 0)
    OP_6E(262, 0)
    OP_6C(315000, 0)
    WaitForThreadExit(0x0008, 0x0001)
    TerminateThread(0x0008, 0x02)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0000)
    ChrSetDirection(0x0008, 180, 500)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0330190957V#841F好了，今天的训练结束了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190958V你们两人都辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190959V#1019F#6P好、好累～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120190960V#813F确、确实……\n',
            '到现在为止最严苛的训练啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0330190961V#843F哎呀哎呀。\n',
            '你们体力还差得太远啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190962V#840F今晚早点休息，\n',
            '准备明天的训练吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190963V#1007F#6P是～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120190964V#1316F您辛苦了～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1500, 0, -1)
    OP_0D()
    OP_23(0x01C3)
    NewScene('ED6_DT21/T5111._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x465
@scena.Code('func_03_465')
def func_03_465():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0201, 3, 0x100B)),
            (Expr.TestScenaFlags, ScenaFlag(0x0203, 3, 0x101B)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4FA',
    )

    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0010190965V#1007F……呼，今天的训练\n',
            '真是够严苛的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190966V#1011F收拾完毕以后\n',
            '可得马上休息才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_4FA(): pass

    label('loc_4FA')

    Return()

# id: 0x0004 offset: 0x4FB
@scena.Code('func_04_4FB')
def func_04_4FB():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　　 游击士协会\n',
            '【卢·洛克尔训练场】',
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
