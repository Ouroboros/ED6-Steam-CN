import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import R2111_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R2111   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'R2111.x'
    header.mapIndex       = 100
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
            word_3A         = 100,
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
        ('ED6_DT07/CH02320._CH', 'ED6_DT07/CH02320P._CP'),
    ]

# id: 0x10001 offset: 0xB2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '基库',
            x                   = 800,
            z                   = 6130,
            y                   = -13810,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0xD2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xD2
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -16740,
            y           = -3000,
            z           = -43910,
            range       = 3000,
            dword_10    = 0x00002710,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000003,
        ),
        ScenaEventData(
            x           = -22290,
            y           = -3000,
            z           = -15520,
            range       = -16120,
            dword_10    = 0x00000000,
            dword_14    = 0xFFFFCFEA,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000005,
        ),
        ScenaEventData(
            x           = -65300,
            y           = -3000,
            z           = -120400,
            range       = -78400,
            dword_10    = 0x00001388,
            dword_14    = 0xFFFE33D8,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000007,
        ),
    )

# id: 0x10004 offset: 0x132
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -16670,
            triggerZ            = -1970,
            triggerY            = -43720,
            triggerRange        = 1500,
            actorX              = -16670,
            actorZ              = -300,
            actorY              = -43720,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -20680,
            triggerZ            = -2009,
            triggerY            = -44860,
            triggerRange        = 1500,
            actorX              = -20680,
            actorZ              = -350,
            actorY              = -44860,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x17A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_191',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_02_1F2)

    def _loc_191(): pass

    label('loc_191')

    Return()

# id: 0x0001 offset: 0x192
@scena.Code('func_01_192')
def func_01_192():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 7, 0x437)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 6, 0x436)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1B4',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, -16940, -1000, -44310, 135)

    def _loc_1B4(): pass

    label('loc_1B4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 6, 0x436)),
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1C9',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1C9(): pass

    label('loc_1C9')

    OP_16(0x02, 4000, -151000, -195000, 196652)
    PlaySE(452, 0x01, 0x64)

    ExecExpressionWithValue(
        0x0008,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0002 offset: 0x1F2
@scena.Code('func_02_1F2')
def func_02_1F2():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(10562, -2000, -118830, 0)
    OP_6C(270000, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, 14150, 1000, -123720, 0)
    ChrSetPos(0x0101, 13220, -2000, -128560, 0)
    ChrSetPos(0x0102, 13220, -2000, -128560, 0)
    ChrSetPos(0x0105, 13220, -2000, -128560, 0)
    ChrSetPos(0x0106, 13220, -2000, -128560, 0)
    PlaySE(140, 0x00, 0x64)

    @scena.Lambda('lambda_0278')
    def lambda_0278():
        OP_6C(315000, 3000)

        ExitThread()

    DispatchAsync(0x0105, 0x0003, lambda_0278)

    @scena.Lambda('lambda_0288')
    def lambda_0288():
        ChrWalkTo(0x00FE, 11270, 3000, -101560, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0288)

    Sleep(1000)

    @scena.Lambda('lambda_02A8')
    def lambda_02A8():
        ChrWalkTo(0x00FE, 13130, -2009, -118750, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_02A8)

    Sleep(500)

    @scena.Lambda('lambda_02C8')
    def lambda_02C8():
        ChrWalkTo(0x00FE, 12380, -1930, -119890, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_02C8)

    Sleep(500)

    @scena.Lambda('lambda_02E8')
    def lambda_02E8():
        ChrWalkTo(0x00FE, 13890, -2040, -119820, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_02E8)

    Sleep(500)

    @scena.Lambda('lambda_0308')
    def lambda_0308():
        ChrWalkTo(0x00FE, 12950, -2009, -120790, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_0308)

    WaitForThreadExit(0x0106, 0x0001)

    ChrTalk(
        0x0106,
        (
            '#0050061126V#052F好像真的是在给我们引路啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050061127V喂，小姑娘。\n',
            '开玩笑的话还是就此打住吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0390')
    def lambda_0390():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0390)

    @scena.Lambda('lambda_039E')
    def lambda_039E():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_039E)

    ChrTurnDirection(0x0105, 0x0106, 400)

    ChrTalk(
        0x0105,
        (
            '#0060061128V#049F#2P我不是在开玩笑。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060061129V因为老师和孩子们\n',
            '就像我的家人一样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050061130V#552F嘁……算了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050061131V大不了\n',
            '就让你骗一次吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061132V#007F#5P你也真是的。\n',
            '一点都不老实。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020061133V#012F#4P先别说了，\n',
            '我们快点跟着基库走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0008, 0x0080)
    EventEnd(0x00)

    Return()

# id: 0x0003 offset: 0x4D1
@scena.Code('func_03_4D1')
def func_03_4D1():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 7, 0x437)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 6, 0x436)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_633',
    )

    MapClearFlags(0x00000001)
    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x0086, 7, 0x437))

    @scena.Lambda('lambda_04ED')
    def lambda_04ED():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_04ED)

    @scena.Lambda('lambda_04FB')
    def lambda_04FB():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_04FB)

    @scena.Lambda('lambda_0509')
    def lambda_0509():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_0509)

    @scena.Lambda('lambda_0517')
    def lambda_0517():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_0517)

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, -17250, 2000, -38520, 315)
    PlaySE(407, 0x00, 0x64)

    @scena.Lambda('lambda_0540')
    def lambda_0540():
        CameraMove(-16010, 2000, -39760, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0540)

    @scena.Lambda('lambda_0558')
    def lambda_0558():
        OP_6C(225000, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_0558)

    OP_97(0x0008, -16030, -39740, -360000, 8000, 0x0001)
    PlaySE(140, 0x00, 0x64)
    OP_97(0x0008, -16030, -39740, -360000, 8000, 0x0001)
    OP_97(0x0008, -16030, -39740, -360000, 8000, 0x0001)

    @scena.Lambda('lambda_05AC')
    def lambda_05AC():
        ChrWalkTo(0x0008, -33520, 5000, -56870, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_05AC)

    PlaySE(140, 0x00, 0x64)
    Sleep(2000)

    OP_69(0x0001, 2000)

    ChrTalk(
        0x0101,
        (
            '#0010061134V#580F那边不就是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061135V#012F嗯……\n',
            '总之先过去看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)
    ChrSetFlags(0x0008, 0x0080)
    MapClearFlags(0x02000000)

    def _loc_633(): pass

    label('loc_633')

    Return()

# id: 0x0004 offset: 0x634
@scena.Code('func_04_634')
def func_04_634():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_656',
    )

    OP_97(0x0008, -16940, -44310, -60000, 9000, 0x0001)
    Yield()

    Jump('func_04_634')

    def _loc_656(): pass

    label('loc_656')

    Return()

# id: 0x0005 offset: 0x657
@scena.Code('func_05_657')
def func_05_657():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 6, 0x436)),
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 0, 0x438)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7CD',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6FA',
    )

    ChrTalk(
        0x0106,
        (
            '#0050061136V#050F没有绕远路的时间了……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050061137V嘁，没办法了。\n',
            '虽然觉得像被捉弄了一样，\n',
            '不过现在也只有赌在那个基库上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7C6')

    def _loc_6FA(): pass

    label('loc_6FA')

    ChrTurnDirection(0x0106, 0x0000, 400)

    ChrTalk(
        0x0106,
        (
            '#0050061138V#050F喂，你们去哪儿。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050061139V现在可没有绕远路的时间啊。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0759')
    def lambda_0759():
        ChrTurnDirection(0x0105, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_0759)

    @scena.Lambda('lambda_0767')
    def lambda_0767():
        ChrTurnDirection(0x0101, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0767)

    ChrTurnDirection(0x0102, 0x0106, 400)

    ChrTalk(
        0x0102,
        (
            '#0020061140V#012F是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061141V现在只能相信基库，\n',
            '跟在它后面追踪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7C6(): pass

    label('loc_7C6')

    Call(0, 0x0006)

    Jump('loc_8A9')

    def _loc_7CD(): pass

    label('loc_7CD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 0, 0x438)),
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_8A9',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_84E',
    )

    ChrTurnDirection(0x0106, 0x0001, 400)

    ChrTalk(
        0x0106,
        (
            '#0050061142V#050F没有绕远路的时间了……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050061143V赶快回灯塔去把这件事搞定吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8A5')

    def _loc_84E(): pass

    label('loc_84E')

    ChrTurnDirection(0x0106, 0x0000, 400)

    ChrTalk(
        0x0106,
        (
            '#0050061144V#050F喂喂，\n',
            '你们打算去散步吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050061145V……赶快回灯塔吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8A5(): pass

    label('loc_8A5')

    Call(0, 0x0006)

    def _loc_8A9(): pass

    label('loc_8A9')

    Return()

# id: 0x0006 offset: 0x8AA
@scena.Code('func_06_8AA')
def func_06_8AA():
    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0007 offset: 0x8C6
@scena.Code('func_07_8C6')
def func_07_8C6():
    If(
        (
            (Expr.Eval, "OP_42(0x0036)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            (Expr.Eval, "OP_29(0x001F, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_969',
    )

    EventBegin(0x01)
    ChrTurnDirection(0x0137, 0x0000, 400)

    ChrTalk(
        0x0137,
        (
            '#1070160718V不好意思，\n',
            '能直接去玛诺利亚村吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0137,
        (
            '#1070160719V我在格兰赛尔\n',
            '还有重要的商谈要进行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_969(): pass

    label('loc_969')

    Return()

# id: 0x0008 offset: 0x96A
@scena.Code('func_08_96A')
def func_08_96A():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '东　卢安市　　　３７４塞尔矩\n',
            '　　玛诺利亚村　　６３塞尔矩',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0009 offset: 0x9D6
@scena.Code('func_09_9D6')
def func_09_9D6():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '南　巴伦诺灯塔　　７０塞尔矩',
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
