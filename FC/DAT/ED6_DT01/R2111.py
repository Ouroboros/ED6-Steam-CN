import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import R2111_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R2111   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '基库'),
    TXT(0x02, ''),
]

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

# id: 0xFFFF offset: 0x9CB
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
            word_3A         = 100,
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
        ('ED6_DT07/CH02320._CH', 'ED6_DT07/CH02320P._CP'),
    ]

# id: 0x10002 offset: 0xB2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
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

# id: 0x10003 offset: 0xD2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0xD2
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

# id: 0x10005 offset: 0x132
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
@scena.Code('PreInit')
def PreInit():
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
    Event(0, 0x0002)

    def _loc_191(): pass

    label('loc_191')

    Return()

# id: 0x0001 offset: 0x192
@scena.Code('Init')
def Init():
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

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, -16940, -1000, -44310, 135)

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
@scena.Code('ReInit')
def ReInit():
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(10562, -2000, -118830, 0)
    OP_6C(270000, 0)
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 14150, 1000, -123720, 0)
    SetChrPos(0x0101, 13220, -2000, -128560, 0)
    SetChrPos(0x0102, 13220, -2000, -128560, 0)
    SetChrPos(0x0105, 13220, -2000, -128560, 0)
    SetChrPos(0x0106, 13220, -2000, -128560, 0)
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

    @scena.Lambda('lambda_0386')
    def lambda_0386():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0386)

    @scena.Lambda('lambda_0394')
    def lambda_0394():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0394)

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
    SetChrFlags(0x0008, 0x0080)
    EventEnd(0x00)

    Return()

# id: 0x0003 offset: 0x4A9
@scena.Code('func_03_4A9')
def func_03_4A9():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 7, 0x437)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 6, 0x436)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_601',
    )

    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x0086, 7, 0x437))

    @scena.Lambda('lambda_04C5')
    def lambda_04C5():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_04C5)

    @scena.Lambda('lambda_04D3')
    def lambda_04D3():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_04D3)

    @scena.Lambda('lambda_04E1')
    def lambda_04E1():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_04E1)

    @scena.Lambda('lambda_04EF')
    def lambda_04EF():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_04EF)

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, -17250, 2000, -38520, 315)
    PlaySE(407, 0x00, 0x64)

    @scena.Lambda('lambda_0518')
    def lambda_0518():
        CameraMove(-16010, 2000, -39760, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0518)

    @scena.Lambda('lambda_0530')
    def lambda_0530():
        OP_6C(225000, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_0530)

    OP_97(0x0008, -16030, -39740, -360000, 8000, 0x0001)
    PlaySE(140, 0x00, 0x64)
    OP_97(0x0008, -16030, -39740, -360000, 8000, 0x0001)
    OP_97(0x0008, -16030, -39740, -360000, 8000, 0x0001)

    @scena.Lambda('lambda_0584')
    def lambda_0584():
        ChrWalkTo(0x0008, -33520, 5000, -56870, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0584)

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
    SetChrFlags(0x0008, 0x0080)
    ClearMapFlags(0x02000000)

    def _loc_601(): pass

    label('loc_601')

    Return()

# id: 0x0004 offset: 0x602
@scena.Code('func_04_602')
def func_04_602():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_624',
    )

    OP_97(0x0008, -16940, -44310, -60000, 9000, 0x0001)
    Yield()

    Jump('func_04_602')

    def _loc_624(): pass

    label('loc_624')

    Return()

# id: 0x0005 offset: 0x625
@scena.Code('func_05_625')
def func_05_625():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 6, 0x436)),
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 0, 0x438)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_77D',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6BE',
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

    Jump('loc_776')

    def _loc_6BE(): pass

    label('loc_6BE')

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

    @scena.Lambda('lambda_0713')
    def lambda_0713():
        ChrTurnDirection(0x0105, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_0713)

    @scena.Lambda('lambda_0721')
    def lambda_0721():
        ChrTurnDirection(0x0101, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0721)

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

    def _loc_776(): pass

    label('loc_776')

    Call(0, 0x0006)

    Jump('loc_845')

    def _loc_77D(): pass

    label('loc_77D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 0, 0x438)),
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_845',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7F4',
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

    Jump('loc_841')

    def _loc_7F4(): pass

    label('loc_7F4')

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

    def _loc_841(): pass

    label('loc_841')

    Call(0, 0x0006)

    def _loc_845(): pass

    label('loc_845')

    Return()

# id: 0x0006 offset: 0x846
@scena.Code('func_06_846')
def func_06_846():
    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0007 offset: 0x862
@scena.Code('func_07_862')
def func_07_862():
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
        'loc_8FB',
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

    def _loc_8FB(): pass

    label('loc_8FB')

    Return()

# id: 0x0008 offset: 0x8FC
@scena.Code('func_08_8FC')
def func_08_8FC():
    FadeOut(300, 0, 100)
    SetChrName('')
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

# id: 0x0009 offset: 0x968
@scena.Code('func_09_968')
def func_09_968():
    FadeOut(300, 0, 100)
    SetChrName('')
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
