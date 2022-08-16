import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C4205_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C4205   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'C4205.x'
    header.mapIndex       = 1
    header.bgm            = 31
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
        ('ED6_DT09/CH10490._CH', 'ED6_DT09/CH10490P._CP'),
        ('ED6_DT09/CH10491._CH', 'ED6_DT09/CH10491P._CP'),
        ('ED6_DT09/CH10500._CH', 'ED6_DT09/CH10500P._CP'),
        ('ED6_DT09/CH10501._CH', 'ED6_DT09/CH10501P._CP'),
        ('ED6_DT09/CH10510._CH', 'ED6_DT09/CH10510P._CP'),
        ('ED6_DT09/CH10511._CH', 'ED6_DT09/CH10511P._CP'),
        ('ED6_DT09/CH11110._CH', 'ED6_DT09/CH11110P._CP'),
        ('ED6_DT09/CH11111._CH', 'ED6_DT09/CH11111P._CP'),
        ('ED6_DT09/CH11120._CH', 'ED6_DT09/CH11120P._CP'),
        ('ED6_DT09/CH11121._CH', 'ED6_DT09/CH11121P._CP'),
        ('ED6_DT09/CH11130._CH', 'ED6_DT09/CH11130P._CP'),
        ('ED6_DT09/CH11131._CH', 'ED6_DT09/CH11131P._CP'),
        ('ED6_DT09/CH11140._CH', 'ED6_DT09/CH11140P._CP'),
        ('ED6_DT09/CH11141._CH', 'ED6_DT09/CH11141P._CP'),
        ('ED6_DT09/CH11150._CH', 'ED6_DT09/CH11150P._CP'),
        ('ED6_DT09/CH11151._CH', 'ED6_DT09/CH11151P._CP'),
    ]

# id: 0x10001 offset: 0x12A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x14A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = -5110,
            z           = 0,
            y           = 48870,
            word_0C     = 0x00B4,
            word_0E     = 0x000C,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0278,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 32880,
            z           = 0,
            y           = 53420,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0280,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 53960,
            z           = 450,
            y           = 101690,
            word_0C     = 0x00B4,
            word_0E     = 0x000E,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x027D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -29030,
            z           = 0,
            y           = 93770,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x026F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -11760,
            z           = 0,
            y           = 93750,
            word_0C     = 0x00B4,
            word_0E     = 0x000C,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0278,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -20280,
            z           = 0,
            y           = 93650,
            word_0C     = 0x00B4,
            word_0E     = 0x000E,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x027D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -31370,
            z           = 1000,
            y           = 112540,
            word_0C     = 0x00B4,
            word_0E     = 0x000E,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0280,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x20E
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x20E
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 57390,
            triggerZ            = 0,
            triggerY            = 52780,
            triggerRange        = 1000,
            actorX              = 58000,
            actorZ              = 1500,
            actorY              = 52910,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x232
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x233
@scena.Code('func_01_233')
def func_01_233():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 7, 0x65F)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_244',
    )

    OP_1B(0x0D, 0x00, 0x0003)

    def _loc_244(): pass

    label('loc_244')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DC, 0, 0x6E0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_256',
    )

    OP_6F(0x0000, 0)

    Jump('loc_25D')

    def _loc_256(): pass

    label('loc_256')

    OP_6F(0x0000, 60)

    def _loc_25D(): pass

    label('loc_25D')

    Return()

# id: 0x0002 offset: 0x25E
@scena.Code('func_02_25E')
def func_02_25E():
    ExecExpressionWithReg(
        0x0001,
        (
            Expr.Rand,
            (Expr.PushLong, 0x8),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_283',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_316')

    def _loc_283(): pass

    label('loc_283')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_29C',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_316')

    def _loc_29C(): pass

    label('loc_29C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B5',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_316')

    def _loc_2B5(): pass

    label('loc_2B5')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2CE',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_316')

    def _loc_2CE(): pass

    label('loc_2CE')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2E7',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_316')

    def _loc_2E7(): pass

    label('loc_2E7')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_300',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_316')

    def _loc_300(): pass

    label('loc_300')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_316',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    def _loc_316(): pass

    label('loc_316')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_32B',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_316')

    def _loc_32B(): pass

    label('loc_32B')

    Return()

# id: 0x0003 offset: 0x32C
@scena.Code('func_03_32C')
def func_03_32C():
    EventBegin(0x00)
    ChrSetDirection(0x0000, 270, 0)
    ChrTurnDirection(0x0001, 0x0000, 0)
    ChrTurnDirection(0x0002, 0x0000, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 6, 0x65E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_46E',
    )

    SetScenaFlags(ScenaFlag(0x00CB, 6, 0x65E))
    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '前面的门被石壁堵塞住了。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0104,
        (
            '#0040131046V#033F咦……\n',
            '难道说这里就是终点了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020131047V#012F嗯，这里的门和刚才一样，\n',
            '设置有隐藏开关。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080131048V#070F呼……\n',
            '正午之前我们就在这里等候吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Jump('loc_4AE')

    def _loc_46E(): pass

    label('loc_46E')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '前面的门被石壁堵塞住了。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    def _loc_4AE(): pass

    label('loc_4AE')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
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
        10,
        0,
        (
            TXT(0x00, '【在这里等到正午】\n'),
            TXT(0x01, '【还要办其他的事】\n'),
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
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000001, 'loc_51B'),
        (0x00000000, 'loc_539'),
        (-1, 'loc_668'),
    )

    def _loc_51B(): pass

    label('loc_51B')

    ChrMoveToRelative(0x0000, 1000, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_668')

    def _loc_539(): pass

    label('loc_539')

    Sleep(100)

    Fade(1000)
    ChrSetPos(0x0102, -20520, 0, 143240, 90)
    ChrSetPos(0x0104, -19330, 0, 142160, 0)
    ChrSetPos(0x0108, -18930, 0, 143850, 225)
    CameraMove(-19500, 0, 143230, 0)
    OP_0D()

    ChrTalk(
        0x0108,
        (
            '#0080131049V#072F好的……\n',
            '在这里等候到正午再说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080131050V时间一到就一口气冲进去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040131051V#035F哈·哈·哈。\n',
            '趁现在好好休息一会儿吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)
    FadeOut(1500, 0, -1)
    OP_0D()
    OP_21()
    ChrSetStatus(0x0000, 0xFE, 0)
    ChrSetStatus(0x0001, 0xFE, 0)
    ChrSetStatus(0x0002, 0xFE, 0)
    ChrSetStatus(0x0003, 0xFE, 0)
    ChrSetStatus(0x0004, 0xFE, 0)
    ChrSetStatus(0x0005, 0xFE, 0)
    ChrSetStatus(0x0006, 0xFE, 0)
    ChrSetStatus(0x0007, 0xFE, 0)
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/R4101._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_668')

    def _loc_668(): pass

    label('loc_668')

    Return()

# id: 0x0004 offset: 0x669
@scena.Code('func_04_669')
def func_04_669():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DC, 0, 0x6E0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_807',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DC, 1, 0x6E1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_745',
    )

    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    ChrSetPos(0x0008, 58000, 3000, 52910, 320)
    ChrTurnDirection(0x0008, 0x0000, 0)

    @scena.Lambda('lambda_06B8')
    def lambda_06B8():
        ChrMoveTo(0x00FE, 58000, 1500, 52910, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_06B8)

    @scena.Lambda('lambda_06D3')
    def lambda_06D3():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1200)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_06D3)

    ChrClearFlags(0x0008, 0x0080)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '魔兽出现了！',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Battle(0x00000270, 0x00000000, 0x00, 0x0000, 0xFF)
    ChrSetFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_720'),
        (0x00000002, 'loc_732'),
        (0x00000001, 'loc_742'),
        (-1, 'loc_745'),
    )

    def _loc_720(): pass

    label('loc_720')

    SetScenaFlags(ScenaFlag(0x00DC, 1, 0x6E1))
    OP_6F(0x0000, 60)
    Sleep(500)

    Jump('loc_745')

    def _loc_732(): pass

    label('loc_732')

    OP_6F(0x0000, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

    def _loc_742(): pass

    label('loc_742')

    OP_B4(0x00)

    Return()

    def _loc_745(): pass

    label('loc_745')

    If(
        (
            (Expr.Eval, "AddItem(0x02D3, 1)"),
            Expr.Return,
        ),
        'loc_797',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '叶隐',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00DC, 0, 0x6E0))

    Jump('loc_804')

    def _loc_797(): pass

    label('loc_797')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '叶隐',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '叶隐',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0)

    def _loc_804(): pass

    label('loc_804')

    Jump('loc_83D')

    def _loc_807(): pass

    label('loc_807')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱里什么东西都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    WaitEffect(0x0F, 0x4D)
    def _loc_83D(): pass

    label('loc_83D')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
