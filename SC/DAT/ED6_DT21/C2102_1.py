import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C2102_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C2102_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0403.x'
    header.mapIndex       = 1
    header.bgm            = 10
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
    ]

# id: 0x10001 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10002 offset: 0xA8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xA8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0xA8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xA8
@scena.Code('Init')
def Init():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_0D()
    Call(1, 0x0007)
    FadeIn(2000, 0)
    Call(1, 0x0008)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1500)

    ChrTalk(
        0x0101,
        (
            '#0010430261V#1004F#4P啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(1, 0x0009)

    If(
        (
            (Expr.Eval, "OP_29(0x0066, 0x01, 0x0001)"),
            Expr.Return,
        ),
        'loc_1BB',
    )

    ChrTalk(
        0x0101,
        (
            '#0010430262V#1020F#2P真、真的在动……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_178',
    )

    ChrTalk(
        0x0106,
        (
            '#0050430263V#057F……和委托人说的一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B8')

    def _loc_178(): pass

    label('loc_178')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_1B8',
    )

    ChrTalk(
        0x0103,
        (
            '#0030430264V#022F……原来如此，和委托人说的一样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B8(): pass

    label('loc_1B8')

    Jump('loc_2BD')

    def _loc_1BB(): pass

    label('loc_1BB')

    ChrTalk(
        0x0101,
        (
            '#0010430265V#1020F#2P好、好像在动啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_253',
    )

    ChrTalk(
        0x0106,
        (
            '#0050430266V#052F……是古代文明的遗物呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050430267V我记得它的功能应该是使机能停止的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2BD')

    def _loc_253(): pass

    label('loc_253')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_2BD',
    )

    ChrTalk(
        0x0103,
        (
            '#0030430268V#022F……是古代文明的遗物呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030430269V我记得它的功能应该是使得机能停止的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2BD(): pass

    label('loc_2BD')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['朵洛希'])"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_469',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0066, 0x01, 0x0001)"),
            Expr.Return,
        ),
        'loc_359',
    )

    ChrTalk(
        0x0104,
        (
            '#0040430270V#031F不过这光真有神秘感。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040430271V嗯，可以让人感受到古人的睿智呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0127,
        (
            '#0280430272V#151F嗯嗯～\n',
            '太漂亮了⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3D8')

    def _loc_359(): pass

    label('loc_359')

    ChrTalk(
        0x0104,
        (
            '#0040430273V#031F原来是古代的装置啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040430274V嗯，怪不得它会发出神秘的光呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0127,
        (
            '#0280430272V#151F嗯嗯～\n',
            '太漂亮了⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3D8(): pass

    label('loc_3D8')

    ChrTurnDirection(0x0101, 0x0127, 400)
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010430276V#1007F#2P怎、怎么还在说些无关紧要的话。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430277V#2P不过，现在看上去\n',
            '倒是没什么危险。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_553')

    def _loc_469(): pass

    label('loc_469')

    If(
        (
            (Expr.Eval, "OP_29(0x0066, 0x01, 0x0001)"),
            Expr.Return,
        ),
        'loc_4E9',
    )

    ChrTalk(
        0x0101,
        (
            '#0010430278V#1015F#2P可是，为什么这种东西\n',
            '会莫名启动呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430277V#2P不过，现在看上去\n',
            '倒是没什么危险。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_553')

    def _loc_4E9(): pass

    label('loc_4E9')

    ChrTalk(
        0x0101,
        (
            '#0010430280V#1020F#2P那、那东西为什么会动啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430281V#1015F不过，现在看上去\n',
            '倒是没什么危险……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_553(): pass

    label('loc_553')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_5C1',
    )

    ChrTalk(
        0x0106,
        (
            '#0050430282V#050F嗯，虽然如此，\n',
            '也不能掉以轻心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050430283V谁都不知道接下来可能会发生什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_634')

    def _loc_5C1(): pass

    label('loc_5C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_634',
    )

    ChrTalk(
        0x0103,
        (
            '#0030430284V#022F嗯，虽然如此，\n',
            '还是不要掉以轻心比较好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030430285V谁都不知道接下来可能会发生什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_634(): pass

    label('loc_634')

    ChrTurnDirection(0x0101, 0x00F7, 400)

    ChrTalk(
        0x0101,
        (
            '#0010430286V#1002F……嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0066, 0x01, 0x2000)
    EventEnd(0x00)

    Return()

# id: 0x0001 offset: 0x66C
@scena.Code('func_01_66C')
def func_01_66C():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_0D()
    Call(1, 0x0007)
    FadeIn(2000, 0)
    Call(1, 0x0008)

    If(
        (
            (Expr.Eval, "OP_29(0x0066, 0x01, 0x2000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6D7',
    )

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1500)

    ChrTalk(
        0x0101,
        (
            '#0010430261V#1004F#4P啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6D7(): pass

    label('loc_6D7')

    Call(1, 0x0009)

    If(
        (
            (Expr.Eval, "OP_29(0x0066, 0x01, 0x2000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_715',
    )

    ChrTalk(
        0x0101,
        (
            '#0010430262V#1020F#2P真、真的在动……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_742')

    def _loc_715(): pass

    label('loc_715')

    ChrTalk(
        0x0101,
        (
            '#0010430295V#1002F#2P果然在活动着呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_742(): pass

    label('loc_742')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['朵洛希'])"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_98E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_782',
    )

    ChrTalk(
        0x0106,
        (
            '#0050430263V#057F……和听说的一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7BE')

    def _loc_782(): pass

    label('loc_782')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_7BE',
    )

    ChrTalk(
        0x0103,
        (
            '#0030430264V#022F……原来如此，和听说的一样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7BE(): pass

    label('loc_7BE')

    ChrTalk(
        0x0104,
        (
            '#0040430270V#031F不过这光真有神秘感。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040430271V嗯，可以让人感受到古人的睿智呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0127,
        (
            '#0280430272V#151F嗯嗯～\n',
            '太漂亮了⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0127, 400)
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010430301V#1007F#2P怎、怎么还在说些无关紧要的话。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430302V#2P快点拍摄完后马上撤退吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_90A',
    )

    ChrTalk(
        0x0106,
        (
            '#0050430303V#552F按我说的办。\n',
            '这里的气氛让人不想久留。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_951')

    def _loc_90A(): pass

    label('loc_90A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_951',
    )

    ChrTalk(
        0x0103,
        (
            '#0030430304V#025F的确如此。\n',
            '这可不是一个让人想久留的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_951(): pass

    label('loc_951')

    ChrSetDirection(0x0101, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010430305V#1015F#2P那么，从哪里开始拍呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B12')

    def _loc_98E(): pass

    label('loc_98E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_A24',
    )

    ChrTalk(
        0x0106,
        (
            '#0050430306V#050F……和听说的一样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050430307V虽然看上去没什么危险，\n',
            '不过还是赶快拍照吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050430308V……这里的气氛让人不想久留。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AC5')

    def _loc_A24(): pass

    label('loc_A24')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_AC5',
    )

    ChrTalk(
        0x0103,
        (
            '#0030430309V#022F……原来如此，和听说的一样呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030430310V虽然看上去没什么危险，\n',
            '不过还是赶快拍照吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030430311V这可不是一个让人想久留的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AC5(): pass

    label('loc_AC5')

    ChrTalk(
        0x0101,
        (
            '#0010430312V#1002F#2P嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430313V#1015F那么，从哪里开始拍呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_B12(): pass

    label('loc_B12')

    OP_59()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※拍摄照片时要使用『#15I导力照相机』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※移动到想拍摄的地方，\n',
            '  请在Camp界面的[Items]标签里\n',
            '  点选『#15I导力照相机』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_59()
    OP_28(0x0066, 0x01, 0x1000)
    OP_28(0x0066, 0x01, 0x2000)
    EventEnd(0x00)

    Return()

# id: 0x0002 offset: 0xBBB
@scena.Code('func_02_BBB')
def func_02_BBB():
    CameraMove(70, 0, 8320, 2000)

    Return()

# id: 0x0003 offset: 0xBCD
@scena.Code('func_03_BCD')
def func_03_BCD():
    ChrSetPos(0x00FE, 600, -1000, -5960, 0)
    Sleep(400)

    ChrMoveToRelative(0x00FE, 600, 0, 6000, 2000, 0x00)

    Return()

# id: 0x0004 offset: 0xBF8
@scena.Code('func_04_BF8')
def func_04_BF8():
    ChrSetPos(0x00FE, -100, -1000, -5960, 0)
    Sleep(400)

    ChrMoveToRelative(0x00FE, -100, 0, 5200, 2000, 0x00)

    Return()

# id: 0x0005 offset: 0xC23
@scena.Code('func_05_C23')
def func_05_C23():
    ChrSetPos(0x00FE, 400, -1000, -5960, 0)
    Sleep(400)

    ChrMoveToRelative(0x00FE, 400, 0, 4200, 2000, 0x00)

    Return()

# id: 0x0006 offset: 0xC4E
@scena.Code('func_06_C4E')
def func_06_C4E():
    ChrSetPos(0x00FE, -300, -1000, -5960, 0)
    Sleep(400)

    ChrMoveToRelative(0x00FE, -300, 0, 3500, 2000, 0x00)

    Return()

# id: 0x0007 offset: 0xC79
@scena.Code('func_07_C79')
def func_07_C79():
    ChrSetPos(0x0101, 600, -10000, -5960, 0)
    ChrSetPos(0x00F7, -600, -10000, -5960, 0)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['朵洛希'])"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_CCA',
    )

    ChrSetPos(0x0104, 600, -10000, -6960, 0)
    ChrSetPos(0x0127, -600, -10000, -6960, 0)

    def _loc_CCA(): pass

    label('loc_CCA')

    Return()

# id: 0x0008 offset: 0xCCB
@scena.Code('func_08_CCB')
def func_08_CCB():
    CreateThread(0x0101, 0x01, 0x01, 0x0003)
    Sleep(750)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_CE8',
    )

    CreateThread(0x0106, 0x01, 0x01, 0x0004)

    Jump('loc_CF6')

    def _loc_CE8(): pass

    label('loc_CE8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_CF6',
    )

    CreateThread(0x0103, 0x01, 0x01, 0x0004)

    def _loc_CF6(): pass

    label('loc_CF6')

    Sleep(750)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['朵洛希'])"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_D1B',
    )

    CreateThread(0x0104, 0x01, 0x01, 0x0005)
    Sleep(750)

    CreateThread(0x0127, 0x01, 0x01, 0x0006)

    def _loc_D1B(): pass

    label('loc_D1B')

    WaitForThreadExit(0x0101, 0x0001)

    Return()

# id: 0x0009 offset: 0xD21
@scena.Code('func_09_D21')
def func_09_D21():
    CameraMove(-160, 950, 12910, 4000)
    Sleep(2000)

    CreateThread(0x0101, 0x02, 0x01, 0x0002)

    @scena.Lambda('lambda_0D44')
    def lambda_0D44():
        ChrMoveToRelative(0x0101, 0, 0, 5000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0D44)

    Sleep(100)

    @scena.Lambda('lambda_0D64')
    def lambda_0D64():
        ChrMoveToRelative(0x00F7, 0, 0, 5000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_0D64)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['朵洛希'])"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_DC6',
    )

    Sleep(100)

    @scena.Lambda('lambda_0D91')
    def lambda_0D91():
        ChrMoveToRelative(0x0104, 0, 0, 5000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_0D91)

    Sleep(100)

    @scena.Lambda('lambda_0DB1')
    def lambda_0DB1():
        ChrMoveToRelative(0x0127, 0, 0, 5000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0127, 0x0001, lambda_0DB1)

    def _loc_DC6(): pass

    label('loc_DC6')

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    Sleep(1000)

    Return()

# id: 0x000A offset: 0xDD6
@scena.Code('func_0A_DD6')
def func_0A_DD6():
    If(
        (
            (Expr.PushValueByIndex, 0x13),
            (Expr.PushLong, 0x232),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E0C',
    )

    MapSetFlags(0x00000080)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '什么也没有发生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    MapClearFlags(0x00000080)

    Return()

    def _loc_E0C(): pass

    label('loc_E0C')

    If(
        (
            (Expr.Eval, "OP_29(0x0066, 0x01, 0x0004)"),
            (Expr.Eval, "OP_29(0x0066, 0x01, 0x0008)"),
            Expr.Or,
            (Expr.Eval, "OP_29(0x0066, 0x00, 0x40)"),
            Expr.Or,
            (Expr.Eval, "OP_29(0x0066, 0x00, 0x08)"),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_E58',
    )

    MapSetFlags(0x00000080)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '什么也没有发生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    MapClearFlags(0x00000080)

    Return()

    def _loc_E58(): pass

    label('loc_E58')

    MapSetFlags(0x00000080)
    OP_C2()
    Sleep(30)

    ChrTurnDirection(0x0009, 0x0000, 0)
    ChrTurnDirection(0x000A, 0x0000, 0)
    ChrTurnDirection(0x000B, 0x0000, 0)
    ChrTurnDirectionByPos(0x0000, -210, 15680, 0)
    ChrTurnDirectionByPos(0x0001, -210, 15680, 0)
    ChrTurnDirectionByPos(0x0002, -210, 15680, 0)
    ChrTurnDirectionByPos(0x0003, -210, 15680, 0)

    If(
        (
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_EC5',
    )

    ExecExpressionWithValue(
        0x0009,
        0x04,
        (
            (Expr.PushLong, 0x168),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    def _loc_EC5(): pass

    label('loc_EC5')

    If(
        (
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_EDE',
    )

    ExecExpressionWithValue(
        0x000A,
        0x04,
        (
            (Expr.PushLong, 0x168),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    def _loc_EDE(): pass

    label('loc_EDE')

    If(
        (
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_EF7',
    )

    ExecExpressionWithValue(
        0x000B,
        0x04,
        (
            (Expr.PushLong, 0x168),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    def _loc_EF7(): pass

    label('loc_EF7')

    If(
        (
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Leq,
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Geq,
            Expr.Nez64,
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Leq,
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0x87),
            Expr.Geq,
            Expr.Nez64,
            Expr.Or,
            Expr.Return,
        ),
        'loc_FA2',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F67',
    )

    ChrTalk(
        0x0101,
        (
            '#0010430314V#1015F从这里拍的话有柱子挡着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F9F')

    def _loc_F67(): pass

    label('loc_F67')

    ChrTalk(
        0x0101,
        (
            '#0010430315V#1015F从那里拍的话可能会被柱子挡到……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F9F(): pass

    label('loc_F9F')

    EventEnd(0x03)

    Return()

    def _loc_FA2(): pass

    label('loc_FA2')

    If(
        (
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x6E),
            Expr.Leq,
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0xFA),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_106D',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_101C',
    )

    ChrTalk(
        0x0101,
        (
            '#0010430316V#1003F这个角度有点不好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430317V得再靠近正面一点拍摄……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_106A')

    def _loc_101C(): pass

    label('loc_101C')

    ChrTalk(
        0x0101,
        (
            '#0010430318V#1007F这个角度有点不好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430319V得再靠近正面一点拍摄。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_106A(): pass

    label('loc_106A')

    EventEnd(0x03)

    Return()

    def _loc_106D(): pass

    label('loc_106D')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushReg, 0x3),
            (Expr.PushReg, 0x2),
            Expr.Sub,
            (Expr.PushReg, 0x3),
            (Expr.PushReg, 0x2),
            Expr.Sub,
            Expr.Mul,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x361A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0005,
        (
            (Expr.PushReg, 0x3),
            (Expr.PushReg, 0x2),
            Expr.Sub,
            (Expr.PushReg, 0x3),
            (Expr.PushReg, 0x2),
            Expr.Sub,
            Expr.Mul,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushReg, 0x5),
            Expr.Add,
            (Expr.PushLong, 0x42C1D80),
            Expr.Leq,
            Expr.Return,
        ),
        'loc_1175',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1126',
    )

    ChrTalk(
        0x0101,
        (
            '#0010430320V#1007F距离有点太近了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430321V可能得再下来一点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1172')

    def _loc_1126(): pass

    label('loc_1126')

    ChrTalk(
        0x0101,
        (
            '#0010430320V#1007F距离有点太近了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430323V可能再下来一点比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1172(): pass

    label('loc_1172')

    EventEnd(0x03)

    Return()

    def _loc_1175(): pass

    label('loc_1175')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushReg, 0x5),
            Expr.Add,
            (Expr.PushLong, 0xBEBC200),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_122A',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11E3',
    )

    ChrTalk(
        0x0101,
        (
            '#0010430324V#1015F………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430325V有点太远了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1227')

    def _loc_11E3(): pass

    label('loc_11E3')

    ChrTalk(
        0x0101,
        (
            '#0010430326V#1015F从那里拍的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430325V有点太远了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1227(): pass

    label('loc_1227')

    EventEnd(0x03)

    Return()

    def _loc_122A(): pass

    label('loc_122A')

    If(
        (
            (Expr.GetChrWork, 0x0, 0x1),
            (Expr.PushLong, 0xFA0),
            Expr.Neg,
            Expr.Lss,
            Expr.Return,
        ),
        'loc_123F',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_13BF')

    def _loc_123F(): pass

    label('loc_123F')

    If(
        (
            (Expr.GetChrWork, 0x0, 0x1),
            (Expr.PushLong, 0xFA0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1253',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_13BF')

    def _loc_1253(): pass

    label('loc_1253')

    If(
        (
            (Expr.GetChrWork, 0x0, 0x3),
            (Expr.PushLong, 0x7D0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1305',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_12BE',
    )

    ChrTalk(
        0x0101,
        (
            '#0010430324V#1015F………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430325V有点太远了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1302')

    def _loc_12BE(): pass

    label('loc_12BE')

    ChrTalk(
        0x0101,
        (
            '#0010430326V#1015F从那里拍的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430325V有点太远了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1302(): pass

    label('loc_1302')

    EventEnd(0x03)

    Return()

    def _loc_1305(): pass

    label('loc_1305')

    If(
        (
            (Expr.GetChrWork, 0x0, 0x3),
            (Expr.PushLong, 0x1838),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_13BF',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1370',
    )

    ChrTalk(
        0x0101,
        (
            '#0010430320V#1007F距离有点太近了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430321V不再下来一点可能不行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13BC')

    def _loc_1370(): pass

    label('loc_1370')

    ChrTalk(
        0x0101,
        (
            '#0010430320V#1007F距离有点太近了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430323V不再下来一点可能不行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13BC(): pass

    label('loc_13BC')

    EventEnd(0x03)

    Return()

    def _loc_13BF(): pass

    label('loc_13BF')

    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1401',
    )

    ChrTalk(
        0x0101,
        (
            '#0010430336V#1015F嗯……\n',
            '从这里会比较好吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14FD')

    def _loc_1401(): pass

    label('loc_1401')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1442',
    )

    ChrTalk(
        0x0106,
        (
            '#0050430337V#050F喂，艾丝蒂尔。\n',
            '这里怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14C1')

    def _loc_1442(): pass

    label('loc_1442')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1483',
    )

    ChrTalk(
        0x0103,
        (
            '#0030430338V#020F艾丝蒂尔。\n',
            '从这里拍怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14C1')

    def _loc_1483(): pass

    label('loc_1483')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_14C1',
    )

    ChrTalk(
        0x0104,
        (
            '#0040430339V#030F艾丝蒂尔。\n',
            '从这里拍怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14C1(): pass

    label('loc_14C1')

    ChrTurnDirectionByPos(0x0101, 0, 12690, 500)

    ChrTalk(
        0x0101,
        (
            '#0010430340V#1011F啊，嗯……\n',
            '确实比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14FD(): pass

    label('loc_14FD')

    FadeOut(300, 0, 100)

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
        100,
        0,
        (
            TXT(0x00, '【从这里拍摄】\n'),
            TXT(0x01, '【找其他地方】\n'),
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1563',
    )

    Call(1, 0x000B)

    Jump('loc_1598')

    def _loc_1563(): pass

    label('loc_1563')

    ChrTalk(
        0x0101,
        (
            '#0010430341V#1015F……再找找\n',
            '别的地方吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_1598(): pass

    label('loc_1598')

    EventEnd(0x03)
    MapClearFlags(0x00000080)

    Return()

# id: 0x000B offset: 0x15A0
@scena.Code('func_0B_15A0')
def func_0B_15A0():
    EventBegin(0x00)
    FadeOut(1000, 0, -1)
    OP_0D()

    ExecExpressionWithValue(
        0x0101,
        0x01,
        (
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0101,
        0x02,
        (
            (Expr.GetChrWork, 0x0, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0101,
        0x03,
        (
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(1)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1636',
    )

    ChrSetDirection(0x0101, 45, 0)
    ChrSetPos(0x00F7, -11490, 250, 4670, 0)
    ChrTurnDirection(0x00F7, 0x0101, 0)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['朵洛希'])"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_1633',
    )

    ChrSetPos(0x0104, -13060, 250, 3460, 0)
    ChrSetPos(0x0127, -11130, 250, 2970, 0)
    ChrTurnDirection(0x0104, 0x0101, 0)
    ChrTurnDirection(0x0127, 0x0101, 0)

    def _loc_1633(): pass

    label('loc_1633')

    Jump('loc_16F8')

    def _loc_1636(): pass

    label('loc_1636')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_169C',
    )

    ChrSetDirection(0x0101, 315, 0)
    ChrSetPos(0x00F7, 12340, 250, 4740, 338)
    ChrTurnDirection(0x00F7, 0x0101, 0)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['朵洛希'])"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_1699',
    )

    ChrSetPos(0x0104, 13400, 250, 3860, 338)
    ChrSetPos(0x0127, 11220, 250, 3250, 338)
    ChrTurnDirection(0x0104, 0x0101, 0)
    ChrTurnDirection(0x0127, 0x0101, 0)

    def _loc_1699(): pass

    label('loc_1699')

    Jump('loc_16F8')

    def _loc_169C(): pass

    label('loc_169C')

    ChrSetDirection(0x0101, 0, 0)
    ChrSetPos(0x00F7, 1050, 0, 500, 0)
    ChrTurnDirection(0x00F7, 0x0101, 0)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['朵洛希'])"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_16F8',
    )

    ChrSetPos(0x0104, 270, 0, -1000, 0)
    ChrSetPos(0x0127, -850, 0, 0, 0)
    ChrTurnDirection(0x0104, 0x0101, 0)
    ChrTurnDirection(0x0127, 0x0101, 0)

    def _loc_16F8(): pass

    label('loc_16F8')

    OP_69(0x0101, 0)
    OP_67(0, 6500, -10000, 0)
    CameraSetDistance(3700, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010430342V#1006F……好，就在这儿了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430343V#1018F那么～我要拍了哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    ChrSetChipByIndex(0x0101, 15)
    OP_0D()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['朵洛希'])"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_17C9',
    )

    ChrTalk(
        0x0127,
        (
            '#0280430344V#151F小艾～加油～⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_17C9(): pass

    label('loc_17C9')

    Sleep(1000)

    Fade(250)
    ChrSetSubChip(0x0101, 1)
    OP_0D()
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(3000)

    OP_63(0x0101)
    Sleep(1000)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['朵洛希'])"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_22BB',
    )

    Fade(250)
    ChrSetSubChip(0x0101, 0)
    OP_0D()
    Sleep(400)

    ChrSetChipByIndex(0x0101, 65535)
    ChrTurnDirection(0x0101, 0x0127, 400)

    ExecExpressionWithValue(
        0x0008,
        0x01,
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.GetChrWork, 0xF7, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x02,
        (
            (Expr.GetChrWork, 0x101, 0x2),
            (Expr.GetChrWork, 0xF7, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x03,
        (
            (Expr.GetChrWork, 0x101, 0x3),
            (Expr.GetChrWork, 0xF7, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x0008, 1000)

    ChrTalk(
        0x0127,
        (
            '#0280430345V#153F咦～要放弃吗～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_18B7',
    )

    ChrTalk(
        0x0106,
        (
            '#0050430346V#052F怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18DD')

    def _loc_18B7(): pass

    label('loc_18B7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_18DD',
    )

    ChrTalk(
        0x0103,
        (
            '#0030430347V#023F怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18DD(): pass

    label('loc_18DD')

    ChrTurnDirection(0x0101, 0x00F7, 400)

    ChrTalk(
        0x0101,
        (
            '#0010430348V#1015F不，我想想觉得\n',
            '没必要一定得让我来拍。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430349V虽说是偶然，不过难得有\n',
            '专家和我们在一起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00F7, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_19A2',
    )

    ChrTalk(
        0x0106,
        (
            '#0050430350V#051F原来是这么回事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19CE')

    def _loc_19A2(): pass

    label('loc_19A2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_19CE',
    )

    ChrTalk(
        0x0103,
        (
            '#0030430351V#021F哦，这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_19CE(): pass

    label('loc_19CE')

    ChrTalk(
        0x0101,
        (
            '#0010430352V#1011F拜托朵洛希了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430353V帮我们拍摄应该没关系吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1A6F',
    )

    ChrTalk(
        0x0106,
        (
            '#0050430354V#051F嗯，没问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050430355V你没自信的话就拜托她吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1ABF')

    def _loc_1A6F(): pass

    label('loc_1A6F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_1ABF',
    )

    ChrTalk(
        0x0103,
        (
            '#0030430356V#027F嗯，没关系。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030430357V你没自信的话就拜托她吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1ABF(): pass

    label('loc_1ABF')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(300, 0, 100)

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
        100,
        0,
        (
            TXT(0x00, '【拜托朵洛希】\n'),
            TXT(0x01, '【自己拍摄】\n'),
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_20E1',
    )

    ChrTurnDirection(0x0101, 0x0127, 400)

    ChrTalk(
        0x0101,
        (
            '#0010430358V#1000F……那么，朵洛希。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430359V可以拜托你来拍吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0127,
        (
            '#0280430360V#151F当然没问题！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280430361V就让我全力以赴地来拍摄吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430362V#1017F嘿嘿，谢谢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430363V那么我把相机给你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1D0C',
    )

    FadeOut(1000, 0, -1)
    OP_0D()
    ChrSetPos(0x0127, 0, 0, 4000, 0)
    ChrSetPos(0x0101, -50, 0, 1280, 0)
    ChrSetPos(0x00F7, 1050, 0, 500, 0)
    ChrTurnDirection(0x00F7, 0x0127, 0)
    ChrSetPos(0x0104, 270, 0, -1000, 0)
    ChrTurnDirection(0x0104, 0x0127, 0)
    OP_69(0x0127, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x0127,
        (
            '#0280430364V#151F那我就开始啰～⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    ChrSetChipByIndex(0x0127, 16)
    OP_0D()
    Call(1, 0x000E)

    ChrTalk(
        0x0127,
        (
            '#0280430365V#153F嘿嘿，很棒的表情～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280210549V#151F来，茄～～子㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    Jump('loc_1EF1')

    def _loc_1D0C(): pass

    label('loc_1D0C')

    @scena.Lambda('lambda_1D12')
    def lambda_1D12():
        OP_69(0x0127, 2000)

        ExitThread()

    DispatchAsync(0x00F7, 0x0002, lambda_1D12)

    @scena.Lambda('lambda_1D20')
    def lambda_1D20():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_1D20')

    DispatchAsync2(0x00F7, 0x0001, lambda_1D20)

    @scena.Lambda('lambda_1D31')
    def lambda_1D31():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_1D31')

    DispatchAsync2(0x0104, 0x0001, lambda_1D31)

    @scena.Lambda('lambda_1D42')
    def lambda_1D42():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_1D42')

    DispatchAsync2(0x0127, 0x0001, lambda_1D42)

    ChrWalkTo(0x0101, -850, 0, 1280, 2000, 0x00)
    ChrTurnDirection(0x0101, 0x0127, 400)
    WaitForThreadExit(0x00F7, 0x0002)
    TerminateThread(0x00F7, 0x01)
    TerminateThread(0x0104, 0x01)
    TerminateThread(0x0127, 0x01)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            '把',
            (TxtCtl.Item, ItemTable['导力照相机']),
            (TxtCtl.SetColor, 0x0),
            '交给了朵洛希。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    Sleep(400)

    ChrTalk(
        0x0127,
        (
            '#0280430367V#150F那么我要开始了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1DF2')
    def lambda_1DF2():
        ChrTurnDirection(0x00FE, 0x0127, 0)
        Yield()

        Jump('lambda_1DF2')

    DispatchAsync2(0x0101, 0x0001, lambda_1DF2)

    OP_94(0x00, 0x0101, 0x010E, 0x00000320, 0x000007D0, 0x00)

    @scena.Lambda('lambda_1E12')
    def lambda_1E12():
        CameraMove(0, 0, 4000, 2000)

        ExitThread()

    DispatchAsync(0x00F7, 0x0002, lambda_1E12)

    @scena.Lambda('lambda_1E2A')
    def lambda_1E2A():
        ChrTurnDirection(0x00FE, 0x0127, 0)
        Yield()

        Jump('lambda_1E2A')

    DispatchAsync2(0x00F7, 0x0001, lambda_1E2A)

    @scena.Lambda('lambda_1E3B')
    def lambda_1E3B():
        ChrTurnDirection(0x00FE, 0x0127, 0)
        Yield()

        Jump('lambda_1E3B')

    DispatchAsync2(0x0104, 0x0001, lambda_1E3B)

    ChrWalkTo(0x0127, -850, 0, 1280, 2000, 0x00)
    ChrWalkTo(0x0127, 0, 0, 4000, 2000, 0x00)
    ChrSetDirection(0x0127, 0, 400)
    TerminateThread(0x00F7, 0x01)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0104, 0x01)
    WaitForThreadExit(0x00F7, 0x0002)
    Sleep(1000)

    Fade(250)
    ChrSetChipByIndex(0x0127, 16)
    OP_0D()
    Call(1, 0x000E)

    ChrTalk(
        0x0127,
        (
            '#0280430365V#153F嘿嘿，很棒的表情～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280430369V#151F那我开始了～来，茄子㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    def _loc_1EF1(): pass

    label('loc_1EF1')

    LoadEffect(0x00, 'map\\\\mp032_00.eff')
    PlaySE(124, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x0127, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(2000)

    ChrSetChipByIndex(0x0127, 65535)
    ChrSetDirection(0x0127, 180, 400)
    Sleep(1000)

    ChrTalk(
        0x0127,
        (
            '#0280430370V#151F让你们久等了～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280430371V我觉得拍得很有韵味哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430372V#1016F真、真像你的风格～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1FCE')
    def lambda_1FCE():
        CameraMove(-850, 0, 1280, 2000)

        ExitThread()

    DispatchAsync(0x00F7, 0x0002, lambda_1FCE)

    @scena.Lambda('lambda_1FE6')
    def lambda_1FE6():
        ChrTurnDirection(0x00FE, 0x0127, 0)
        Yield()

        Jump('lambda_1FE6')

    DispatchAsync2(0x0101, 0x0001, lambda_1FE6)

    @scena.Lambda('lambda_1FF7')
    def lambda_1FF7():
        ChrTurnDirection(0x00FE, 0x0127, 0)
        Yield()

        Jump('lambda_1FF7')

    DispatchAsync2(0x00F7, 0x0001, lambda_1FF7)

    @scena.Lambda('lambda_2008')
    def lambda_2008():
        ChrTurnDirection(0x00FE, 0x0127, 0)
        Yield()

        Jump('lambda_2008')

    DispatchAsync2(0x0104, 0x0001, lambda_2008)

    ChrWalkTo(0x0127, -850, 0, 1280, 2000, 0x00)
    ChrTurnDirection(0x0127, 0x0101, 400)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x00F7, 0x01)
    TerminateThread(0x0104, 0x01)
    WaitForThreadExit(0x00F7, 0x0002)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.Item, ItemTable['导力照相机']),
            (TxtCtl.SetColor, 0x0),
            '归还了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#0010430373V#1001F嗯，不过还是要谢谢你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430374V好了，这样拍摄的任务就完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0066, 0x01, 0x0008)

    Jump('loc_22B8')

    def _loc_20E1(): pass

    label('loc_20E1')

    ChrTalk(
        0x0101,
        (
            '#0010430375V#1015F……虽然这么想，\n',
            '不过还是由我来拍吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430376V因为这是我自己接下的工作。\n',
            '必须靠自己坚持到底才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0127,
        (
            '#0280430377V#150F嗯，难得有这个机会，\n',
            '还是让小艾来拍比较好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280430378V毕竟把这么棒的模特儿\n',
            '让给别人来拍，也太可惜了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430379V#1007F抱歉，朵洛希。\n',
            '搞得这么大动干戈的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirectionByPos(0x0101, -210, 15680, 400)

    ChrTalk(
        0x0101,
        (
            '#0010430380V#1002F好，重新准备。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430381V再次集中精力来拍摄照片了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    ChrSetChipByIndex(0x0101, 15)
    OP_0D()
    Sleep(400)

    Fade(250)
    ChrSetSubChip(0x0101, 1)
    OP_0D()
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(2000)

    OP_63(0x0101)
    Sleep(1000)

    Call(1, 0x000C)
    OP_28(0x0066, 0x01, 0x0004)
    def _loc_22B8(): pass

    label('loc_22B8')

    Jump('loc_22C5')

    def _loc_22BB(): pass

    label('loc_22BB')

    Call(1, 0x000C)
    OP_28(0x0066, 0x01, 0x0004)
    def _loc_22C5(): pass

    label('loc_22C5')

    If(
        (
            (Expr.Eval, "OP_29(0x0066, 0x01, 0x0004)"),
            Expr.Return,
        ),
        'loc_22D4',
    )

    Call(1, 0x000F)

    def _loc_22D4(): pass

    label('loc_22D4')

    Call(1, 0x000D)
    EventEnd(0x00)

    Return()

# id: 0x000C offset: 0x22DB
@scena.Code('func_0C_22DB')
def func_0C_22DB():
    LoadEffect(0x00, 'map\\\\mp032_00.eff')
    PlaySE(124, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x0101, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(2000)

    Fade(250)
    ChrSetSubChip(0x0101, 0)
    OP_0D()
    Sleep(400)

    ChrSetChipByIndex(0x0101, 65535)
    ChrTurnDirection(0x0101, 0x00F7, 400)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010430382V#1018F好，拍摄完毕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Return()

# id: 0x000D offset: 0x2376
@scena.Code('func_0D_2376')
def func_0D_2376():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_23CD',
    )

    ChrTalk(
        0x0106,
        (
            '#0050430383V#050F那么马上回城里吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050430384V待在这里也没什么用了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_242F')

    def _loc_23CD(): pass

    label('loc_23CD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_242F',
    )

    ChrTalk(
        0x0103,
        (
            '#0030430385V#020F那么马上回城里吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030430386V一直待在这种地方也没什么太大的意义。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_242F(): pass

    label('loc_242F')

    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x0101, 0x00F7, 400)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010430387V#1004F咦？要回去了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_24C4',
    )

    ChrTalk(
        0x0106,
        (
            '#0050430388V#052F嗯，是这么打算的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050430389V有什么问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2512')

    def _loc_24C4(): pass

    label('loc_24C4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_2512',
    )

    ChrTalk(
        0x0103,
        (
            '#0030430390V#023F嗯，是这么打算的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030430391V有什么问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2512(): pass

    label('loc_2512')

    ChrTalk(
        0x0101,
        (
            '#0010430392V#1015F倒是没有什么问题……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430393V不过难得来到这里，\n',
            '马上回去的话是不是有点可惜？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_25EE',
    )

    ChrTalk(
        0x0106,
        (
            '#0050430394V#051F咦，怎么了？\n',
            '你还想探索这座塔吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050430395V如果你有这个想法\n',
            '我就陪你一起去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2653')

    def _loc_25EE(): pass

    label('loc_25EE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_2653',
    )

    ChrTalk(
        0x0103,
        (
            '#0030430396V#027F咦，想探索这座塔吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030430397V如果你这么想的话，\n',
            '我倒是没什么问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2653(): pass

    label('loc_2653')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(300, 0, 100)

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
        100,
        0,
        (
            TXT(0x00, '【马上返回卢安】\n'),
            TXT(0x01, '【探索完塔之后再返回】\n'),
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_283F',
    )

    ChrTalk(
        0x0101,
        (
            '#0010430398V#1007F抱歉，还是算了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430399V首先要把照片的工作\n',
            '完成才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_276F',
    )

    ChrTalk(
        0x0106,
        (
            '#0050430400V#053F啊啊，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050430401V#050F好，直接返回城里吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27BB')

    def _loc_276F(): pass

    label('loc_276F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_27BB',
    )

    ChrTalk(
        0x0103,
        (
            '#0030430402V#020F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030430403V那么，直接返回城里吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_27BB(): pass

    label('loc_27BB')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['朵洛希'])"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_280B',
    )

    ChrTalk(
        0x0104,
        (
            '#0040430404V#031F嗯，那么走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0127,
        (
            '#0280430405V#151F好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2833')

    def _loc_280B(): pass

    label('loc_280B')

    ChrTalk(
        0x0101,
        (
            '#0010430406V#1006F嗯！　我们走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2833(): pass

    label('loc_2833')

    NewScene('ED6_DT21/T2101._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_2A16')

    def _loc_283F(): pass

    label('loc_283F')

    ChrTalk(
        0x0101,
        (
            '#0010430407V#1006F嗯，还是想先去\n',
            '探索一下哟。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430408V这里也有很多挺厉害的魔兽，\n',
            '可以当成一次不错的训练。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2925',
    )

    ChrTalk(
        0x0106,
        (
            '#0050430409V#053F的确如此\n',
            '正好可以舒展一下筋骨……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050430410V#051F好，那我们\n',
            '就稍微绕点远路吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_299E')

    def _loc_2925(): pass

    label('loc_2925')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_299E',
    )

    ChrTalk(
        0x0103,
        (
            '#0030430411V#021F呵呵，的确如此\n',
            '正好可以舒展一下筋骨……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030430412V#020F明白了，那我们\n',
            '就稍微绕点远路吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_299E(): pass

    label('loc_299E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['朵洛希'])"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_29EE',
    )

    ChrTalk(
        0x0104,
        (
            '#0040430404V#031F嗯，那么走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0127,
        (
            '#0280430405V#151F好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A16')

    def _loc_29EE(): pass

    label('loc_29EE')

    ChrTalk(
        0x0101,
        (
            '#0010430415V#1006F嗯！　就这么办。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A16(): pass

    label('loc_2A16')

    Return()

# id: 0x000E offset: 0x2A17
@scena.Code('func_0E_2A17')
def func_0E_2A17():
    OP_62(0x0127, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(400)

    OP_94(0x01, 0x0127, 0x005A, 0x000001F4, 0x000003E8, 0x00)
    Sleep(800)

    OP_94(0x01, 0x0127, 0x010E, 0x000003E8, 0x000003E8, 0x00)
    Sleep(200)

    OP_94(0x01, 0x0127, 0x005A, 0x000001F4, 0x000003E8, 0x00)
    Sleep(400)

    OP_94(0x01, 0x0127, 0x00B4, 0x000001F4, 0x000003E8, 0x00)
    Sleep(800)

    OP_63(0x0127)

    Return()

# id: 0x000F offset: 0x2A82
@scena.Code('func_0F_2A82')
def func_0F_2A82():
    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.PushLong, 0x32),
            Expr.Neg,
            Expr.Geq,
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.PushLong, 0x32),
            Expr.Leq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2AB1',
    )

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2C28')

    def _loc_2AB1(): pass

    label('loc_2AB1')

    If(
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.PushLong, 0x2710),
            Expr.Neg,
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2ACD',
    )

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x8),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2C28')

    def _loc_2ACD(): pass

    label('loc_2ACD')

    If(
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.PushLong, 0x1F40),
            Expr.Neg,
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2AE9',
    )

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x7),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2C28')

    def _loc_2AE9(): pass

    label('loc_2AE9')

    If(
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.PushLong, 0xFA0),
            Expr.Neg,
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2B05',
    )

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x6),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2C28')

    def _loc_2B05(): pass

    label('loc_2B05')

    If(
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2B21',
    )

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x5),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2C28')

    def _loc_2B21(): pass

    label('loc_2B21')

    If(
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.PushLong, 0x3E8),
            Expr.Neg,
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2B3D',
    )

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x4),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2C28')

    def _loc_2B3D(): pass

    label('loc_2B3D')

    If(
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.PushLong, 0x1F4),
            Expr.Neg,
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2B59',
    )

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x3),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2C28')

    def _loc_2B59(): pass

    label('loc_2B59')

    If(
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.PushLong, 0x32),
            Expr.Neg,
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2B75',
    )

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2C28')

    def _loc_2B75(): pass

    label('loc_2B75')

    If(
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.PushLong, 0x2710),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2B8F',
    )

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2C28')

    def _loc_2B8F(): pass

    label('loc_2B8F')

    If(
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.PushLong, 0x1F40),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2BA9',
    )

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2C28')

    def _loc_2BA9(): pass

    label('loc_2BA9')

    If(
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.PushLong, 0xFA0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2BC3',
    )

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2C28')

    def _loc_2BC3(): pass

    label('loc_2BC3')

    If(
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.PushLong, 0x7D0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2BDD',
    )

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2C28')

    def _loc_2BDD(): pass

    label('loc_2BDD')

    If(
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.PushLong, 0x3E8),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2BF7',
    )

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2C28')

    def _loc_2BF7(): pass

    label('loc_2BF7')

    If(
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.PushLong, 0x1F4),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2C11',
    )

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2C28')

    def _loc_2C11(): pass

    label('loc_2C11')

    If(
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.PushLong, 0x32),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2C28',
    )

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2C28(): pass

    label('loc_2C28')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
