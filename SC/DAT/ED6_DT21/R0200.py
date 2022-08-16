import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import R0200_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R0200   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'R0200.x'
    header.mapIndex       = 22
    header.bgm            = 29
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
        ('ED6_DT09/CH10020._CH', 'ED6_DT09/CH10020P._CP'),
        ('ED6_DT09/CH10021._CH', 'ED6_DT09/CH10021P._CP'),
        ('ED6_DT09/CH10180._CH', 'ED6_DT09/CH10180P._CP'),
        ('ED6_DT09/CH10181._CH', 'ED6_DT09/CH10181P._CP'),
        ('ED6_DT09/CH10260._CH', 'ED6_DT09/CH10260P._CP'),
        ('ED6_DT09/CH10261._CH', 'ED6_DT09/CH10261P._CP'),
        ('ED6_DT09/CH10210._CH', 'ED6_DT09/CH10210P._CP'),
        ('ED6_DT09/CH10211._CH', 'ED6_DT09/CH10211P._CP'),
        ('ED6_DT29/CH12090._CH', 'ED6_DT29/CH12090P._CP'),
        ('ED6_DT29/CH12091._CH', 'ED6_DT29/CH12091P._CP'),
    ]

# id: 0x10001 offset: 0xFA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '洛连特方向',
            x                   = -48570,
            z                   = 0,
            y                   = -24070,
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
            name                = '威尔特桥·关所方向',
            x                   = -143230,
            z                   = 0,
            y                   = -17530,
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

# id: 0x10002 offset: 0x13A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '跳跳猫',
            x           = -78000,
            z           = 0,
            y           = -16000,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0079,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '爆种铃兰',
            x           = -92600,
            z           = 0,
            y           = -13700,
            word_0C     = 0x00A0,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x007A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '混合',
            x           = -121000,
            z           = 0,
            y           = -31000,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x007E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '大食人花',
            x           = -108000,
            z           = 0,
            y           = 1800,
            word_0C     = 0x00E4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x007D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '爆种铃兰',
            x           = -103000,
            z           = 0,
            y           = -25600,
            word_0C     = 0x000A,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x007A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '跳跳猫',
            x           = -118000,
            z           = 0,
            y           = -8000,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0079,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '红茶钳虫',
            x           = -81000,
            z           = 0,
            y           = -36000,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x007B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x1FE
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x1FE
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -105260,
            triggerZ            = 0,
            triggerY            = 14600,
            triggerRange        = 1000,
            actorX              = -104710,
            actorZ              = 1500,
            actorY              = 14910,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -74510,
            triggerZ            = 0,
            triggerY            = -19420,
            triggerRange        = 1500,
            actorX              = -74510,
            actorZ              = 1500,
            actorY              = -19420,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -118840,
            triggerZ            = -90,
            triggerY            = 3750,
            triggerRange        = 1000,
            actorX              = -116330,
            actorZ              = -500,
            actorY              = 6430,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x26A
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x26B
@scena.Code('func_01_26B')
def func_01_26B():
    OP_16(0x02, 4000, -226000, -148000, 2293771)

    ExecExpressionWithVar(
        0x3A,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_298',
    )

    OP_10(0x01, 0x00)
    OP_10(0x02, 0x01)

    def _loc_298(): pass

    label('loc_298')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0324, 0, 0x1920)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2AA',
    )

    OP_6F(0x0000, 0)

    Jump('loc_2B1')

    def _loc_2AA(): pass

    label('loc_2AA')

    OP_6F(0x0000, 60)

    def _loc_2B1(): pass

    label('loc_2B1')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2F7',
    )

    OP_C4(0x00, 0x00000004)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_2E2',
    )

    MapSetFlags(0x00000010)
    OP_11(0xE6, 0xF0, 0xFF, 0, 60000, 0)

    Jump('loc_2F7')

    def _loc_2E2(): pass

    label('loc_2E2')

    MapSetFlags(0x00000010)
    OP_11(0xE6, 0xF0, 0xFF, 0, 80000, 0)

    def _loc_2F7(): pass

    label('loc_2F7')

    ExecExpressionWithValue(
        0x000A,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0002 offset: 0x345
@scena.Code('func_02_345')
def func_02_345():
    UnlockAchievement(0x02, 0x01C1, 0x00)
    MapSetFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0324, 0, 0x1920)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3E0',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    OP_73(0x0000)
    OP_6F(0x0000, 60)
    AddSepith(0x01, 100)
    AddSepith(0x03, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#57I水之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x2),
            '#59I风之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    SetScenaFlags(ScenaFlag(0x0324, 0, 0x1920))

    Jump('loc_3FA')

    def _loc_3E0(): pass

    label('loc_3E0')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_3FA(): pass

    label('loc_3FA')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x40C
@scena.Code('func_03_40C')
def func_03_40C():
    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0011860001V#1001F这里好像可以钓上什么来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0444')
    def lambda_0444():
        CameraMove(-117210, -110, 4810, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0444)

    @scena.Lambda('lambda_045C')
    def lambda_045C():
        CameraSetDistance(2800, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_045C)

    @scena.Lambda('lambda_046C')
    def lambda_046C():
        OP_6C(270000, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_046C)

    Sleep(1000)

    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '钓鱼吗？',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        32,
        1,
        (
            TXT(0x00, '钓鱼\n'),
            TXT(0x01, '离开\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    WaitForThreadExit(0x0000, 0x0001)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5B9',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.GetChrWork, 0x101, 0x28),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0101,
        0x28,
        (
            (Expr.PushLong, 0x1),
            Expr.Not,
            Expr.And2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.Eval, "OP_C0(0x0E, 0x00000001, 0xFFFE2FC8, 0xFFFFFFA6, 0x00000EA6, 0x0000002D, 0xFFFE3996, 0xFFFFFE0C, 0x0000191E)"),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0101,
        0x28,
        (
            (Expr.PushReg, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_5B3',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0073, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x0073, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0073, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5AD',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0073, 0x01, 0x0008)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5AA',
    )

    OP_28(0x0073, 0x01, 0x0002)
    OP_28(0x0073, 0x01, 0x0008)
    Sleep(400)

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '将在米尔西街道发现钓鱼场的事情\n',
            '记录在游击士手册上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    def _loc_5AA(): pass

    label('loc_5AA')

    Jump('loc_5B3')

    def _loc_5AD(): pass

    label('loc_5AD')

    OP_28(0x0073, 0x01, 0x0800)

    def _loc_5B3(): pass

    label('loc_5B3')

    OP_0D()
    EventEnd(0x01)

    Jump('loc_5C8')

    def _loc_5B9(): pass

    label('loc_5B9')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5C8',
    )

    EventEnd(0x01)

    def _loc_5C8(): pass

    label('loc_5C8')

    Return()

# id: 0x0004 offset: 0x5C9
@scena.Code('func_04_5C9')
def func_04_5C9():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '东　洛连特市\n',
            '西　威尔特桥　１７２塞尔矩',
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
