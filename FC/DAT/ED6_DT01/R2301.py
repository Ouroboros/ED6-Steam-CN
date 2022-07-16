import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import R2301_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R2301   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '梅威海道方向'),
    TXT(0x02, '杰尼丝王立学院方向'),
    TXT(0x03, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'R2301.x'
    header.mapIndex       = 102
    header.bgm            = 21
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x7AB
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
            word_3A         = 102,
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
        ('ED6_DT09/CH10520._CH', 'ED6_DT09/CH10520P._CP'),
        ('ED6_DT09/CH10521._CH', 'ED6_DT09/CH10521P._CP'),
        ('ED6_DT09/CH10340._CH', 'ED6_DT09/CH10340P._CP'),
        ('ED6_DT09/CH10341._CH', 'ED6_DT09/CH10341P._CP'),
        ('ED6_DT09/CH11040._CH', 'ED6_DT09/CH11040P._CP'),
        ('ED6_DT09/CH11041._CH', 'ED6_DT09/CH11041P._CP'),
        ('ED6_DT09/CH11070._CH', 'ED6_DT09/CH11070P._CP'),
        ('ED6_DT09/CH11071._CH', 'ED6_DT09/CH11071P._CP'),
        ('ED6_DT09/CH11080._CH', 'ED6_DT09/CH11080P._CP'),
        ('ED6_DT09/CH11081._CH', 'ED6_DT09/CH11081P._CP'),
    ]

# id: 0x10002 offset: 0xFA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 128320,
            z                   = 20,
            y                   = -8070,
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
        ScenaNpcData(
            x                   = 288640,
            z                   = 10,
            y                   = -9980,
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

# id: 0x10003 offset: 0x13A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = 164610,
            z           = 540,
            y           = -8970,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0196,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 161500,
            z           = -30,
            y           = -7250,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0196,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 193850,
            z           = 320,
            y           = -43450,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0192,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 218740,
            z           = 0,
            y           = -37100,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0194,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 235120,
            z           = -10,
            y           = -3610,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0193,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 230490,
            z           = 130,
            y           = -5740,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0195,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 210450,
            z           = 10,
            y           = -27270,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0192,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 164610,
            z           = 540,
            y           = -8970,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x033A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 161500,
            z           = -30,
            y           = -7250,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x033A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 193850,
            z           = 320,
            y           = -43450,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0336,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 218740,
            z           = 0,
            y           = -37100,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0338,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 235120,
            z           = -10,
            y           = -3610,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0337,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 230490,
            z           = 130,
            y           = -5740,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0339,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 210450,
            z           = 10,
            y           = -27270,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0336,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x2C2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x2C2
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x2C2
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_2E5',
    )

    OP_B1('R2301_y')
    SetScenaFlags(ScenaFlag(0x0086, 4, 0x434))

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0xE),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x0002)

    def _loc_2E5(): pass

    label('loc_2E5')

    Return()

# id: 0x0001 offset: 0x2E6
@scena.Code('Init')
def Init():
    OP_16(0x02, 4000, 85000, -154000, 196650)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_310',
    )

    OP_B1('R2301_y')

    Jump('loc_319')

    def _loc_310(): pass

    label('loc_310')

    OP_B1('R2301_n')

    def _loc_319(): pass

    label('loc_319')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_34B',
    )

    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000F, 0x0080)
    SetChrFlags(0x0010, 0x0080)

    Jump('loc_36E')

    def _loc_34B(): pass

    label('loc_34B')

    SetChrFlags(0x0011, 0x0080)
    SetChrFlags(0x0012, 0x0080)
    SetChrFlags(0x0013, 0x0080)
    SetChrFlags(0x0014, 0x0080)
    SetChrFlags(0x0015, 0x0080)
    SetChrFlags(0x0016, 0x0080)
    SetChrFlags(0x0017, 0x0080)

    def _loc_36E(): pass

    label('loc_36E')

    Return()

# id: 0x0002 offset: 0x36F
@scena.Code('ReInit')
def ReInit():
    SetScenaFlags(ScenaFlag(0x0086, 4, 0x434))
    EventBegin(0x00)
    CameraMove(275050, 0, -9400, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 287750, 10, -9520, 90)
    SetChrPos(0x0102, 287750, 10, -10870, 90)
    SetChrPos(0x0105, 287750, 20, -10050, 90)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_03F3')
    def lambda_03F3():
        ChrWalkTo(0x00FE, 270940, 50, -9520, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_03F3)

    Sleep(500)

    @scena.Lambda('lambda_0413')
    def lambda_0413():
        ChrWalkTo(0x00FE, 271020, -10, -10870, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0413)

    Sleep(500)

    @scena.Lambda('lambda_0433')
    def lambda_0433():
        ChrWalkTo(0x00FE, 272280, -20, -10050, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_0433)

    @scena.Lambda('lambda_044E')
    def lambda_044E():
        CameraMove(272170, 0, -9340, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_044E)

    WaitForThreadExit(0x0101, 0x0001)
    SetChrDirection(0x0101, 180, 400)
    WaitForThreadExit(0x0102, 0x0001)
    ChrTurnDirection(0x0102, 0x0101, 400)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010060939V#001F#1P嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060940V虽然只有几天，\n',
            '但真的很开心呢～！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060941V#008F当然呢，上课这个除外。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020060942V#017F#4P你这是什么\n',
            '本末倒置的话啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060943V#018F本来上课才是主业，\n',
            '学园祭只是特别活动嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010060944V#007F#1P那也是啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060945V唉，原来不管在哪里\n',
            '做学生都是那么辛苦的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060060946V#045F#2P呵呵……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060060947V#044F……咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0105, 180, 400)
    Sleep(200)

    SetChrDirection(0x0105, 0, 400)
    Sleep(200)

    SetChrDirection(0x0105, 90, 400)
    Sleep(500)

    OP_62(0x0105, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_0624')
    def lambda_0624():
        ChrTurnDirection(0x0101, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0624)

    ChrTurnDirection(0x0102, 0x0105, 400)

    ChrTalk(
        0x0102,
        (
            '#0020060948V#014F#4P怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060060949V#043F#2P没什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060060950V我觉得基库\n',
            '好像不在这附近……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060060951V到哪里去了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060952V#501F#3P嘿嘿，\n',
            '可能是去找吃的了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060060953V#045F#2P是啊……\n',
            '那也可能是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060060954V对不起。\n',
            '突然说了些奇怪的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060060955V#040F那么，在出海道之前，\n',
            '就让我们一起上路吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060956V#001F#3P嗯⊙\n',
            '慢慢走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearMapFlags(0x10000000)
    ClearMapFlags(0x02000000)
    OP_20(0x000003E8)
    EventEnd(0x00)
    OP_21()
    PlayBGM(21)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
