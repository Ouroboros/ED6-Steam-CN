import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T2600_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2600   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2600.x'
    header.mapIndex       = 1
    header.bgm            = 32
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
        ('ED6_DT27/CH03001._CH', 'ED6_DT27/CH03001P._CP'),
        ('ED6_DT27/CH03011._CH', 'ED6_DT27/CH03011P._CP'),
        ('ED6_DT27/CH03091._CH', 'ED6_DT27/CH03091P._CP'),
        ('ED6_DT27/CH03131._CH', 'ED6_DT27/CH03131P._CP'),
    ]

# id: 0x10001 offset: 0xCA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '王立学院·小道',
            x                   = 170,
            z                   = 0,
            y                   = -16239,
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

# id: 0x10002 offset: 0xEA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xEA
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -1600,
            y           = 1000,
            z           = 9950,
            range       = 1600,
            dword_10    = 0x000007D0,
            dword_14    = 0x000020E4,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000009,
        ),
    )

# id: 0x10004 offset: 0x10A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 33200,
            triggerZ            = 0,
            triggerY            = 14520,
            triggerRange        = 1000,
            actorX              = 32570,
            actorZ              = 0,
            actorY              = 14530,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x12E
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_141',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    Event(0, func_03_2D7)

    def _loc_141(): pass

    label('loc_141')

    Return()

# id: 0x0001 offset: 0x142
@scena.Code('func_01_142')
def func_01_142():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0268, 0, 0x1340)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_154',
    )

    OP_6F(0x0002, 0)

    Jump('loc_15B')

    def _loc_154(): pass

    label('loc_154')

    OP_6F(0x0002, 60)

    def _loc_15B(): pass

    label('loc_15B')

    OP_16(0x02, 4000, -128000, -106000, 2293838)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_177',
    )

    Jump('loc_18C')

    def _loc_177(): pass

    label('loc_177')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 7, 0x201F)),
            Expr.Return,
        ),
        'loc_18C',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x59),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x02000000)

    def _loc_18C(): pass

    label('loc_18C')

    Return()

# id: 0x0002 offset: 0x18D
@scena.Code('func_02_18D')
def func_02_18D():
    UnlockAchievement(0x02, 0x01FD, 0x00)
    MapSetFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0268, 0, 0x1340)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2AB',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 30)
    OP_73(0x0002)
    OP_6F(0x0002, 30)
    AddSepith(0x00, 10)
    AddSepith(0x01, 10)
    AddSepith(0x02, 10)
    AddSepith(0x03, 10)
    AddSepith(0x04, 10)
    AddSepith(0x05, 10)
    AddSepith(0x06, 10)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#56I地之耀晶片×１０\n',
            (TxtCtl.SetColor, 0x2),
            '#57I水之耀晶片×１０\n',
            (TxtCtl.SetColor, 0x2),
            '#58I火之耀晶片×１０\n',
            (TxtCtl.SetColor, 0x2),
            '#59I风之耀晶片×１０\n',
            (TxtCtl.SetColor, 0x2),
            '#62I时之耀晶片×１０\n',
            (TxtCtl.SetColor, 0x2),
            '#60I空之耀晶片×１０\n',
            (TxtCtl.SetColor, 0x2),
            '#61I幻之耀晶片×１０\n',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    SetScenaFlags(ScenaFlag(0x0268, 0, 0x1340))

    Jump('loc_2C5')

    def _loc_2AB(): pass

    label('loc_2AB')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_2C5(): pass

    label('loc_2C5')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x2D7
@scena.Code('func_03_2D7')
def func_03_2D7():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_DB()
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x010A, 0x0080)
    ChrSetFlags(0x010E, 0x0080)
    ChrSetFlags(0x0102, 0x0040)
    ChrSetFlags(0x0101, 0x0040)
    ChrSetFlags(0x010A, 0x0040)
    ChrSetFlags(0x010E, 0x0040)
    ChrSetFlags(0x0102, 0x0004)
    ChrSetFlags(0x0101, 0x0004)
    ChrSetFlags(0x010A, 0x0004)
    ChrSetFlags(0x010E, 0x0004)
    ChrSetPos(0x0102, 29770, 0, 14350, 0)
    ChrSetPos(0x0101, 29770, 0, 14350, 0)
    ChrSetPos(0x010A, 29770, 0, 14350, 0)
    ChrSetPos(0x010E, 29770, 0, 14350, 0)
    CameraMove(-210, 0, 1470, 0)
    OP_67(0, 12190, -10000, 0)
    CameraSetDistance(4030, 0)
    OP_6C(45000, 0)
    OP_6E(294, 0)
    OP_11(0x44, 0x42, 0x79, 39700, 89900, 0)
    CreateThread(0x0102, 0x02, 0x00, func_04_624)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_03C7')
    def lambda_03C7():
        CameraMove(24700, 0, 13240, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_03C7)

    WaitForThreadExit(0x0101, 0x0000)
    Fade(500)
    OP_11(0x44, 0x42, 0x79, 39700, 75000, 0)
    CameraMove(25650, 0, 15090, 0)
    OP_67(0, 7380, -10000, 0)
    CameraSetDistance(3040, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    CreateThread(0x0102, 0x01, 0x00, func_05_679)
    Sleep(1000)

    CreateThread(0x0101, 0x01, 0x00, func_06_6D1)
    Sleep(1000)

    CreateThread(0x010A, 0x01, 0x00, func_07_715)
    Sleep(1000)

    CreateThread(0x010E, 0x01, 0x00, func_08_759)
    WaitForThreadExit(0x010E, 0x0001)
    TerminateThread(0x0102, 0x02)
    OP_DC()

    ChrTalk(
        0x0101,
        (
            '#0010360805V#1002F#5P……开始了呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120360806V#812F#5P嗯，我们也得赶快了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360807V#1035F#5P这前面就是学院后门，\n',
            '刚才已经把锁打开了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020360808V#1040F应该可以马上打开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010E,
        (
            '#0330360809V#843F#5P明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330360810V#842F立即进入各设施，\n',
            '救出被拘束的人们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330360811V已救出的人在手册的『人质名单』\n',
            '里检查就行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360812V#1005F#5P明白！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120360813V#816F#5PＬｅｔ＇ｓ　ｇｏ！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x00C0, 0x01, 0x0004)
    OP_28(0x00C0, 0x01, 0x0008)
    OP_28(0x00C0, 0x01, 0x0010)
    OP_28(0x00C0, 0x01, 0x0020)
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

# id: 0x0004 offset: 0x624
@scena.Code('func_04_624')
def func_04_624():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_678',
    )

    PlaySE(565, 0x00, 0x3C)
    Sleep(1500)

    OP_23(0x0235)
    Sleep(500)

    PlaySE(565, 0x00, 0x3C)
    Sleep(1900)

    OP_23(0x0235)
    Sleep(700)

    PlaySE(565, 0x00, 0x3C)
    Sleep(1700)

    OP_23(0x0235)
    Sleep(600)

    PlaySE(565, 0x00, 0x3C)
    Sleep(2000)

    OP_23(0x0235)
    Sleep(800)

    Jump('func_04_624')

    def _loc_678(): pass

    label('loc_678')

    Return()

# id: 0x0005 offset: 0x679
@scena.Code('func_05_679')
def func_05_679():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetChipByIndex(0x00FE, 1)
    ChrSetFlags(0x00FE, 0x1000)
    ChrWalkTo(0x00FE, 26760, 0, 14350, 5000, 0x00)
    ChrWalkTo(0x00FE, 23780, 0, 14350, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 65535)
    ChrSetSubChip(0x00FE, 0)
    ChrClearFlags(0x00FE, 0x1000)
    ChrSetDirection(0x00FE, 225, 400)
    ChrClearFlags(0x00FE, 0x0040)
    ChrClearFlags(0x00FE, 0x0004)

    Return()

# id: 0x0006 offset: 0x6D1
@scena.Code('func_06_6D1')
def func_06_6D1():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetChipByIndex(0x00FE, 0)
    ChrSetFlags(0x00FE, 0x1000)
    ChrWalkTo(0x00FE, 24730, 0, 13360, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 65535)
    ChrSetSubChip(0x00FE, 0)
    ChrClearFlags(0x00FE, 0x1000)
    ChrSetDirection(0x00FE, 225, 400)
    ChrClearFlags(0x00FE, 0x0040)
    ChrClearFlags(0x00FE, 0x0004)

    Return()

# id: 0x0007 offset: 0x715
@scena.Code('func_07_715')
def func_07_715():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetChipByIndex(0x00FE, 2)
    ChrSetFlags(0x00FE, 0x1000)
    ChrWalkTo(0x00FE, 25010, 0, 15300, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 65535)
    ChrSetSubChip(0x00FE, 0)
    ChrClearFlags(0x00FE, 0x1000)
    ChrSetDirection(0x00FE, 225, 400)
    ChrClearFlags(0x00FE, 0x0040)
    ChrClearFlags(0x00FE, 0x0004)

    Return()

# id: 0x0008 offset: 0x759
@scena.Code('func_08_759')
def func_08_759():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetChipByIndex(0x00FE, 3)
    ChrSetFlags(0x00FE, 0x1000)
    ChrWalkTo(0x00FE, 26000, 0, 14500, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 65535)
    ChrSetSubChip(0x00FE, 0)
    ChrClearFlags(0x00FE, 0x1000)
    ChrSetDirection(0x00FE, 225, 400)
    ChrClearFlags(0x00FE, 0x0040)
    ChrClearFlags(0x00FE, 0x0004)

    Return()

# id: 0x0009 offset: 0x79D
@scena.Code('func_09_79D')
def func_09_79D():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 7, 0x201F)),
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 6, 0x202E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_8F2',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7FA',
    )

    ChrTalk(
        0x0101,
        (
            '#0010360814V#1002F（没工夫磨磨蹭蹭了。\n',
            '　得赶快去学院啊。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8D2')

    def _loc_7FA(): pass

    label('loc_7FA')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_83F',
    )

    ChrTalk(
        0x0102,
        (
            '#0020360815V#1042F（时间有限。\n',
            '　赶快去学院吧。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8D2')

    def _loc_83F(): pass

    label('loc_83F')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_88B',
    )

    ChrTalk(
        0x010A,
        (
            '#0120360816V#816F（不必去这栋建筑吧。\n',
            '　赶快去学院吧。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8D2')

    def _loc_88B(): pass

    label('loc_88B')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8D2',
    )

    ChrTalk(
        0x010E,
        (
            '#0330360817V#842F（应该不必去这边。\n',
            '　赶快去学院吧。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8D2(): pass

    label('loc_8D2')

    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    MapSetFlags(0x02000000)

    def _loc_8F2(): pass

    label('loc_8F2')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
